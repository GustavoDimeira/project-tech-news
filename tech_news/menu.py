import sys


# Requisitos 11 e 12
def analyzer_menu():
    try:
        option = int(input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.\n"""))
        if (option < 0 or option > 5):
            raise ValueError

    except ValueError:
        sys.stderr.write('Invalid option\n')
