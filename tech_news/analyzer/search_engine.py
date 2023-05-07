from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    response = []
    query = {"title": {"$regex": title, "$options": "i"}}
    items = search_news(query)

    for item in items:
        response.append((item["title"], item["url"]))

    return response


# Requisito 8
def search_by_date(date):
    try:
        response = []

        iso_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")

        query = {"timestamp": {"$eq": iso_date}}
        items = search_news(query)

        for item in items:
            response.append((item["title"], item["url"]))

        return response
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    response = []
    query = {"category": {"$regex": category, "$options": "i"}}
    items = search_news(query)

    for item in items:
        response.append((item["title"], item["url"]))

    return response
