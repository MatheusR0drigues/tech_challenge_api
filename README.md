# Documentação Detalhada

## 1. Introdução
### Objetivo da API
Esta API fornece acesso a dados extraídos do site da Embrapa sobre a produção, processamento, comercialização, importação e exportação de vinhos e derivados. Os dados estão disponíveis para os anos entre 1970 e 2022. A API foi projetada para coletar e organizar dados de forma estruturada, servindo como uma fonte de informações confiável e atualizada para alimentar bases de dados que serão utilizadas em modelos de machine learning. Estes modelos visam analisar tendências da indústria, otimizar processos e prever comportamentos do mercado de vinhos e derivados.

### Público-alvo
Desenvolvedores, cientistas de dados e pesquisadores que estão interessados em analisar tendências do mercado de vinhos e derivados. A API é ideal para aqueles que precisam de dados históricos e recentes para treinar modelos preditivos ou realizar análises estatísticas avançadas.

### Informações Gerais
A API é acessada via HTTP, retornando dados em formato JSON. Não é necessário autenticação no momento, facilitando o acesso para análises preliminares e desenvolvimento de aplicações.

## 2. Endpoints
### [GET] /dados/{ano}/{opcao}/{subopcao}
- **Descrição:** Este endpoint recupera dados especificados pelo ano, opção e, quando aplicável, subopção.
- **Parâmetros:**
  - `ano`: Ano dos dados (1970 a 2022).
  - `opcao`: Categoria dos dados:
    - `opt_02`: Produção (não requer subopção).
    - `opt_03`: Processamento.
      - `subopt_01`: Viníferas
      - `subopt_02`: Americanas e híbridas
      - `subopt_03`: Uvas de mesa
      - `subopt_04`: Sem classificação
    - `opt_04`: Comercialização (não requer subopção).
    - `opt_05`: Importação.
      - `subopt_01`: Vinhos de mesa
      - `subopt_02`: Espumantes
      - `subopt_03`: Uvas frescas
      - `subopt_04`: Uvas passas
      - `subopt_05`: Suco de uva
    - `opt_06`: Exportação.
      - `subopt_01`: Vinhos de mesa
      - `subopt_02`: Espumantes
      - `subopt_03`: Uvas frescas
      - `subopt_04`: Suco de uva

## 4. Manuseio de Erros
- **400 Bad Request:** Ano fora do intervalo permitido, ou opção/subopção inválida.
- **404 Not Found:** Nenhum dado encontrado para os parâmetros fornecidos.
- **500 Internal Server Error:** Erro interno do servidor.

# 5. Funcionalidades

- **Extração Automatizada:** Coleta dados automaticamente do site da Embrapa conforme configurado.
- **Endpoints de API:** Fornece vários endpoints para acessar dados sobre produção, processamento, e mais.
- **Dados em Formato JSON:** Todos os dados são retornados em formato JSON, facilitando a integração com outras aplicações e sistemas.

# 6. Tecnologias Utilizadas

- **Flask:** Framework web utilizado para construir a API.
- **Requests:** Biblioteca utilizada para realizar requisições HTTP ao site da Embrapa.
- **BeautifulSoup:** Biblioteca usada para fazer o parsing das páginas HTML obtidas do site da Embrapa.
