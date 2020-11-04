''' Scripts to get mobile phone pages on amazon'''


from bs4 import BeautifulSoup
import requests
url = "https://www.amazon.in/s?k=smartphones&ref=nb_sb_noss"

# add header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

file = open(r"mobile_links.txt", "w")

links = soup.find_all(
    'a', {'class': 'a-link-normal a-text-normal'})

for link in links:
    # print(link.get('href'))
    amazon_link = 'http://amazon.in' + link.get('href')
    file.write(amazon_link + '\n')
file.close()
