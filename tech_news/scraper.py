from tech_news.database import create_news
from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"})
        if (not response.status_code == 200):
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    response_list = []

    selector = Selector(text=html_content)
    links = selector.css(".cs-overlay-link::attr(href)").getall()

    for link in links:
        response_list.append(link)

    return response_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    button = selector.css(".next::attr(href)").get()

    try:
        return button
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    response = {}

    response["url"] = selector.css("link[rel='canonical']::attr(href)").get()
    response["title"] = selector.css(".entry-title::text").get().strip()
    response["timestamp"] = selector.css(".meta-date::text").get()
    response["writer"] = selector.css(".author a::text").get()
    response["reading_time"] = int(
        selector.css(".meta-reading-time::text").get().split(" ")[0]
    )
    response["summary"] = (
        selector.css(".entry-content p").xpath("string()").get().strip()
    )
    response["category"] = selector.css(".label::text").get()

    return response


# Requisito 5
def get_tech_news(amount):
    response = []
    links = []
    page_link = "https://blog.betrybe.com"

    while(len(links) < amount):
        page = fetch(page_link)
        for link in scrape_updates(page):
            links.append(link)
        page_link = scrape_next_page_link(page)

    for i in range(amount):
        response.append(scrape_news(fetch(links[i])))

    create_news(response)
    return response
