import requests
from bs4 import BeautifulSoup
from settings import URL_BASE

def extrair_dados(ano, opcao, subopcao):
    url = f"{URL_BASE}?ano={ano}&opcao={opcao}&subopcao={subopcao}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='tb_base tb_dados')
    
    if table:
        cabeçalhos = [th.text.strip() for th in table.find('tr').find_all('th')]
        dados = []
        linhas = table.find_all('tr')[1:]
        for row in linhas:
            colunas = row.find_all('td')
            dados.append({cabeçalhos[i]: col.text.strip() for i, col in enumerate(colunas)})
        return dados
    else:
        return []  # Retorna lista vazia se não encontrar a tabela
