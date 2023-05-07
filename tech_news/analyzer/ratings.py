from tech_news.database import find_news


def to_sort(list):
    sort_by_name = sorted(list, key=lambda item: item[0])
    sort_by_value = sorted(sort_by_name, key=lambda item: -item[1])

    return sort_by_value


def get_value(list):
    response = []
    counter = 0
    for k, v in list:
        counter += 1
        if counter <= 5:
            response.append(k)

    return response


# Requisito 10
def top_5_categories():
    types_dict = {}
    news = find_news()

    for new in news:
        try:
            types_dict[new["category"]] += 1
        except KeyError:
            types_dict[new["category"]] = 1

    sorted_dict = to_sort(types_dict.items())
    response = get_value(sorted_dict)

    return response


print(top_5_categories())
