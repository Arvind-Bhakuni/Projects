import requests, random
from bs4 import BeautifulSoup
import pprint

def scrapewikiarticle(url):
    response = requests.get(url)

    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id='firstHeading')
    print("Title : ",title.string)
    print("All wiki links on this page scraped below: ")

    # Get all the link
    links = soup.find(id='bodyContent').find_all('a')
    random.shuffle(links)
    scraped_links = dict()

    for link in links:
        url = link.get('href', "")
        if "/wiki/" in url:
            scraped_links[link.text.strip()] = url

    print("Article Name  :  Link")
    for k,v in scraped_links.items():
        print(f"{k} : {v}")

url="https://en.wikipedia.org/wiki/Web_scraping"
scrapewikiarticle(url)