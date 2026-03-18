# Bibliotecas utilizadas para automação, manipulação do sistema e controle de execução
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from os import system, name
from datetime import datetime
import sys

# Obtém a data e hora atual formatada no padrão brasileiro
data_hora_atual = datetime.now()
data_hora_formatada = data_hora_atual.strftime('%d/%m/%Y %H:%M')

# Função que limpa o terminal
def limpar_terminal():
    system('cls' if name == 'nt' else 'clear')


# Mensagem indicando para o usuario que a aplicação irá iniciar o site desejado
print("Acessando o site para Web Scraping")

# Inicia o navegador e acessa a pagina para extração de dados
driver = webdriver.Chrome()
driver.get("https://economia.uol.com.br/cotacoes/cambio/")

# Exibe animação de carregamento no terminal
spinner = ['|', '/', '-', '\\']
for i in range(20):
    sys.stdout.write(f"\rColetando Dados {spinner[i % len(spinner)]}")
    sys.stdout.flush()
    sleep(0.2)

# Coleta de dados
# Localiza o container e extrai o valor interno (evitando conflito de classes repetidas)
container_dolar_pay = driver.find_element(By.CLASS_NAME, "chart-info-pay") # Coletando o valor atual de compra do dolar
cotacao_dolar_pay = container_dolar_pay.find_element(
    By.CLASS_NAME, "chart-info-val").text

container_dolar_buy = driver.find_element(By.CLASS_NAME, "chart-info-buy") # Coletando o valor atual de venda do dolar
cotacao_dolar_buy = container_dolar_buy.find_element(
    By.CLASS_NAME, "chart-info-val").text

container_dolar_max = driver.find_element(By.CLASS_NAME, "chart-info-max") # Coletando o valor maximo do dolar no dia 
cotacao_dolar_max = container_dolar_max.find_element(
    By.CLASS_NAME, "chart-info-val").text


container_dolar_min = driver.find_element(By.CLASS_NAME, "chart-info-min") # Coletando o valor minimo do dolar no dia
cotacao_dolar_min = container_dolar_min.find_element(
    By.CLASS_NAME, "chart-info-val").text

# Faz a limpeza do terminal para uma melhor visualização dos dados
limpar_terminal()

# Exibe os dados coletados junto da data e hora da coleta
print(
    f"""=-=-=-=-=-=DADOS COLETADOS=-=-=-=-=-=
DATA DA COLETA: {data_hora_formatada}

VALOR ATUAL DE COMPRA DO DOLAR: {cotacao_dolar_pay}
VALOR ATUAL DE VENDA DO DOLAR: {cotacao_dolar_buy}
VALOR MAXIMO DO DOLAR (DIA): {cotacao_dolar_max}
VALOR MINIMO DO DOLAR(DIA): {cotacao_dolar_min}""")
