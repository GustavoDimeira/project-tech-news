from tech_news.scraper import get_tech_news
# from tech_news.database import create_news
from tech_news.analyzer.search_engine import search_by_title
from tech_news.analyzer.search_engine import search_by_date
from tech_news.analyzer.search_engine import search_by_category
from tech_news.analyzer.ratings import top_5_categories
import sys


select_option_text = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.\n"""


def op0():
    amount = int(input("Digite quantas notícias serão buscadas:\n"))
    news = get_tech_news(amount)
    # create_news(news)
    print(news)


def op1():
    title = input("Digite o título:\n")
    print(search_by_title(title))


def op2():
    date = input("Digite a data no formato aaaa-mm-dd:\n")
    search_by_date(date)


def op3():
    category = input("Digite a categoria:\n")
    print(search_by_category(category))


def op4():
    print(top_5_categories())


def op5():
    print("Encerrando script")


ops = [op0, op1, op2, op3, op4, op5]


# Requisitos 11 e 12
def analyzer_menu():
    try:
        option = int(input(select_option_text))

        if (option < 0 or option > 5):
            raise ValueError
        ops[option]()

    except ValueError:
        sys.stderr.write('Opção inválida\n')
