<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Um projeto que tem como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias podem ser obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

  <strong>🚵 Habilidades a serem trabalhadas:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
    <li>Aplicar técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
  </ul>

</details>

# Orientações

<details>

  1. Clone o repositório

* Entre na pasta do repositório que você acabou de clonar:
  * `cd sd-023-a-tech-news`

  2. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├── tech_news
  │   ├── analyzer
  │   │   ├── 🔹ratings.py
  │   │   ├── 🔸reading_plan.py
  │   │   └── 🔹search_engine.py
  │   ├── 🔸database.py
  │   └── 🔹menu.py
  │   └── 🔹scraper.py
  ├── tests
  │   ├── reading_plan
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_reading_plan.py
  │   ├── 🔸assets/*
  │   ├── 🔸__init__.py
  │   ├── 🔸marker.py
  │   ├── 🔸test_menu.py
  │   ├── 🔸test_ratings.py
  │   ├── 🔸test_scraper.py
  │   └── 🔸test_search_engine.py
  ├── 🔸dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  ├── 🔸setup.py
  ├── 🔸trybe-filter-repo.sh
  └── 🔸trybe.yml
  ```

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso queira executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso queira executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  <strong>✍️ Teste Manual</strong>
  
  Abra um terminal Python importando as funções de interesse através do comando:

  <code>python3 -i tech_news/arquivo_de_interesse.py</code>

</details>

<details>
  <summary><strong>🐳Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm news pytest
  ```

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  As notícias a serem raspadas estarão disponíveis no _Blog da Trybe_: https://blog.betrybe.com.
  Essas notícias devem ser salvas no banco de dados utilizando as funções python que já vêm prontas no módulo `database.py`

  <strong>MongoDB</strong>

  Para a realização deste projeto, utilizaremos um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.
  Já existem algumas funções prontas no arquivo `tech_news/database.py` que te auxiliarão no desenvolvimento.
  Não altere as funções deste arquivo; mudanças nele não serão executadas no avaliador automático.

  Rodar MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal.
  Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:

  Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>
  MacOS:  <https://docs.mongodb.com/guides/server/install/>
  
  Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.

</details>


# Requisitos obrigatórios

## 1 - Crie a função `fetch`

local: `tech_news/scraper.py`

Antes de fazer scrape, precisamos de uma página! Esta função será responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.

* A função deve receber uma URL
* A função deve fazer uma requisição HTTP `get` para esta URL utilizando a função `requests.get`
* A função deve retornar o conteúdo HTML da resposta.
* A função deve respeitar um Rate Limit de 1 requisição por segundo; Ou seja, caso chamada múltiplas vezes, ela deve aguardar 1 segundo entre cada requisição que fizer.
* Caso a requisição seja bem sucedida com `Status Code 200: OK`, deve ser retornado seu conteúdo de texto;
* Caso a resposta tenha o código de status diferente de `200`, deve-se retornar `None`;
* Caso a requisição não receba resposta em até 3 segundos, ela deve ser abandonada (este caso é conhecido como "Timeout") e a função deve retornar None.

📌 Você vai precisar definir o _header_ `user-agent` para que a raspagem do blog da Trybe funcione corretamente. Para isso, preencha com o valor `"Fake user-agent"` conforme exemplo abaixo:

```python
{ "user-agent": "Fake user-agent" }
```

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:

  `python3 -i tech_news/scraper.py`

  Agora invoque as funções utilizando diferentes parâmetros.
  Exemplo:

  ```python
  html = fetch(url_da_noticia)
  scrape_news(html)
  ```

</details>

## 2 - Crie a função `scrape_updates`

local: `tech_news/scraper.py`

Esta função fará o scrape da página para obter as URLs das páginas de notícias. Vamos utilizar as ferramentas que aprendemos no curso, como a biblioteca Parsel, para obter os dados que queremos de cada página.

* A função deve receber uma string com o conteúdo HTML da página inicial do blog
* A função deve fazer o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
* A função deve retornar esta lista.
* Caso não encontre nenhuma URL de notícia, a função deve retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python importando estas funções através do comando:
  
  `python3 -i tech_news/scraper.py`
  
  Agora invoque as funções utilizando diferentes parâmetros. Exemplo:

  ```python
  html = fetch(url_da_noticia)
  scrape_updates(html)
  ```

</details>

## 3 - Crie a função `scrape_next_page_link`

local: `tech_news/scraper.py`

* A função deve receber como parâmetro uma `string` contendo o conteúdo HTML da página de novidades (<https://blog.betrybe.com>)
* A função deve fazer o scrape deste HTML para obter a URL da próxima página.
* A função deve retornar a URL obtida.
* Caso não encontre o link da próxima página, a função deve retornar `None`

## 4 - Crie a função `scrape_news`

local: `tech_news/scraper.py`

* A função deve receber como parâmetro o conteúdo HTML da página de uma única notícia
* A função deve, no conteúdo recebido, buscar as informações das notícias para preencher um dicionário com os seguintes atributos:
  * `url` - link para acesso da notícia.
  * `title` - título da notícia.
  * `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
  * `writer` - nome da pessoa autora da notícia.
  * `reading_time` - número de minutos necessários para leitura.
  * `summary` - o primeiro parágrafo da notícia.
  * `category` - categoria da notícia.

* Exemplo de um retorno da função com uma notícia fictícia:

```json
{
  "url": "https://blog.betrybe.com/novidades/noticia-bacana",
  "title": "Notícia bacana",
  "timestamp": "04/04/2021",
  "writer": "Eu",
  "reading_time": 4,
  "summary": "Algo muito bacana aconteceu",
  "category": "Ferramentas",
}
  ```

## 5 - Crie a função `get_tech_news` para obter as notícias

local: `tech_news/scraper.py`

* A função deve receber como parâmetro um número inteiro `n` e buscar as últimas `n` notícias do site.
* Utilize as funções `fetch`, `scrape_updates`, `scrape_next_page_link` e `scrape_news` para buscar as notícias e processar seu conteúdo.
* As notícias buscadas devem ser inseridas no MongoDB; Para acessar o banco de dados, importe e utilize as funções que já temos prontas em `tech_news/database.py`
* Após inserir as notícias no banco, a função deve retornar estas mesmas notícias.

Rodar MongoDB via Docker: `docker-compose up -d mongodb` no terminal.
Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:
Ubuntu: <https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/>  
MacOS:  <https://docs.mongodb.com/guides/server/install/>


## 6 - Teste a classe `ReadingPlanService`

local: `tests/reading_plan/test_reading_plan.py`

O serviço de **planejamento de leituras**, implementado no arquivo `tech_news/analyzer/reading_plan.py`, coleta as notícias do banco de dados e as divide em 2 agrupamentos:

1. `readable`: notícias que podem ser lidas em até `X` minutos
2. `unreadable`: notícias que **não** podem ser lidas em até `X` minutos

Além disso, as notícias `readable` são organizadas em sub-grupos cuja soma dos tempos de leitura seja menor que `X`. Assim, a pessoa leitora pode ler mais do que 1 notícia sem ultrapassar o tempo disponível!

O valor de `X`, que é o tempo de leitura que uma pessoa tem disponível, é passado por parâmetro no método `group_news_for_available_time`, que é um **método de classe**.


## 7 - Crie a função `search_by_title`

local: `tech_news/analyzer/search_engine.py`

* A função deve receber uma string com um título de notícia
* A função deve buscar as notícias do banco de dados por título
* A função deve retornar uma lista de tuplas com as notícias encontradas nesta busca.
Exemplo:

```python
[
  ("Título1_aqui", "url1_aqui"),
  ("Título2_aqui", "url2_aqui"),
  ("Título3_aqui", "url3_aqui"),
]
```

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_title("Algoritmos")`.

</details>

## 8 - Crie a função `search_by_date`

local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias do banco de dados por data.

* A função deve receber como parâmetro uma data no formato ISO `AAAA-mm-dd`
* A função deve buscar as notícias do banco de dados por data.
* A função deve ter retorno no mesmo formato do requisito anterior.
* Caso a data seja inválida, ou esteja em outro formato, uma exceção `ValueError` deve ser lançada com a mensagem `Data inválida`.
* Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_date("2021-04-04")`

</details>

## 9 - Crie a função `search_by_category`

local: `tech_news/analyzer/search_engine.py`

Esta função irá buscar as notícias por categoria.

* A função deve receber como parâmetro o nome da categoria completo.
* A função deve buscar as notícias do banco de dados por categoria.
* A função deve ter retorno no mesmo formato do requisito anterior.
* Caso nenhuma notícia seja encontrada, deve-se retornar uma lista vazia.
* A busca deve ser _case insensitive_

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/search_engine.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `search_by_category("Ferramentas")`.
</details>


## 10 - Crie a função `top_5_categories`

local: `tech_news/analyzer/ratings.py`

Esta função irá listar as cinco categorias com maior ocorrência no banco de dados.

* A função deve buscar as categorias do banco de dados e calcular a sua "popularidade" com base no número de ocorrências;
* As top 5 categorias da análise devem ser retornadas em uma lista no formato `["category1", "category2"]`;
* A ordem das categorias retornadas deve ser da mais popular para a menos popular, ou seja, categorias que estão em mais notícias primeiro;
* Em caso de empate, o desempate deve ser por ordem alfabética de categoria.
* Caso haja menos de cinco categorias, no banco de dados, deve-se retornar todas as categorias existentes;
* Caso não haja categorias disponíveis, deve-se retornar uma lista vazia.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>
  Abra um terminal Python importando esta função através do comando:
  
  `python3 -i tech_news/analyzer/ratings.py`
  
  Agora invoque a função utilizando diferentes parâmetros. Exemplo:
  
  `top_5_categories()`.

</details>
