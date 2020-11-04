import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings


class ReviewSpider(scrapy.Spider):

    name = 'review_spider'
    allowed_domains = ['amazon.in']

    f = open('mobile_links.txt', 'r+')
    my_file_data = f.read()
    f.close()
    start_urls = my_file_data.split("\n")

    # start_urls = ['https://www.amazon.in/Apple-iPhone-11-128GB-Black/dp/B07XVLW7YK/ref=sr_1_2_sspa?dchild=1&keywords=smartphones&qid=1603027064&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMUxPR1hRWDY1SFlWJmVuY3J5cHRlZElkPUEwMzcxMDQ1VEo5UEowRkdKVkdRJmVuY3J5cHRlZEFkSWQ9QTA5NDI3ODcyNUdWOUkzTDRWUVVHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==']

    def parse(self, response):

        ratings = response.xpath(
            '//i[contains(concat(" ",normalize-space(@class)," ")," review-rating ")]/span/text()').extract()

# #
        reviews = response.xpath(
            'string(//div[contains(@class, "review-text-content")])').extract()

        count = 0

        for item in zip(reviews, ratings):
            data = {
                'Review': item[0],
                'Label': item[1],
            }

        # for item in ratings:
        #     data = {"rating": item}

        yield data
        count += 1


if __name__ == '__main__':
    spidy = ReviewSpider()
    print(spidy.start_urls)

    process = CrawlerProcess()
    process.crawl(ReviewSpider)
    process.start()
