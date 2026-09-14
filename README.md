# Projeto AMA

## Descrição

Projeto para monitorar as mamadas da minha filha utilizando uma base de dados em estrela (star schema) em SQLite, processamento em Python e criação de relatórios com Power BI e HTML.

## Requisitos

- Python 3.x
- Flask
- SQLite

## Instalação

1. Clone o repositório:
sh git clone <https://github.com/yourusername/ama-project.git>

2. Crie e ative um ambiente virtual (opcional):
sh python -m venv venv
source venv/bin/activate  # No Windows use venv\Scripts\activate

3. Instale as dependências:
sh pip install -r requirements.txt

## Banco de Dados

Para criar a base de dados, execute o script `create_database.py`:

sh python create_database.py

## API

A API permite criar, ler, atualizar e deletar mamadas. Para executar a API, execute o script `api.py`:

sh python api.py

## Relatórios

1. **Power BI**: Configure Power BI para conectar-se ao banco de dados SQLite e crie visualizações simples mostrando a frequência diária e média de mamadas por hora.
2. **HTML Dash**: Crie um dash simples mostrando que você pode personalizar o layout conforme necessário.
