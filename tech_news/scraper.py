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
    links = selector.css(".cs-overlay-link").getall()

    for link in links:
        response_list.append(
            link.split('<a href="')[1].split('" class="cs-overlay-link">')[0])

    return response_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    button = selector.css(".next").get()

    try:
        return button.split('href="')[1].split('">Próxima</a>')[0]
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


print(scrape_next_page_link(fetch("https://blog.betrybe.com/page/2/")))
