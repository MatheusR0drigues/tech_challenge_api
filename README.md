# API de Dados da Embrapa

## Descrição
Este projeto consiste em uma API desenvolvida em Flask que extrai e disponibiliza dados sobre a produção, processamento, comercialização, importação e exportação de vinhos e derivados a partir do site da Embrapa. O objetivo desta API é fornecer uma interface programática fácil de usar para acessar dados históricos e recentes, que podem ser utilizados para análises estatísticas, desenvolvimento de modelos de previsão em machine learning e suporte à decisão em negócios relacionados ao setor de vinhos e derivados.

## Funcionalidades
- **Extração Automatizada**: Coleta dados automaticamente do site da Embrapa conforme configurado.
- **Endpoints de API**: Fornece vários endpoints para acessar dados sobre produção, processamento, e mais.
- **Dados em Formato JSON**: Todos os dados são retornados em formato JSON, facilitando a integração com outras aplicações e sistemas.

## Tecnologias Utilizadas
- **Flask**: Framework web utilizado para construir a API.
- **Requests**: Biblioteca utilizada para realizar requisições HTTP ao site da Embrapa.
- **BeautifulSoup**: Biblioteca usada para fazer o parsing das páginas HTML obtidas do site da Embrapa.
