# Web Scraping de Cotações de Câmbio

## 📋 Descrição

Aplicação Python que realiza web scraping para extrair cotações do dólar em tempo real do site de economia da UOL. O programa coleta informações de compra, venda, máximo e mínimo do dólar e exibe os dados com a data e hora da coleta.

## 🚀 Funcionalidades

- **Coleta de Cotações**: Extrai dados de compra e venda do dólar
- **Valores Extremos**: Obtém os valores máximo e mínimo do dia
- **Timestamp**: Registra a data e hora da coleta no formato brasileiro (DD/MM/YYYY HH:MM)
- **Animação de Carregamento**: Exibe spinner animado durante o processamento
- **Interface Limpa**: Terminal limpo para melhor visualização dos resultados

## 📦 Dependências

- **Python 3.8+** (recomendado 3.10+)
- **Selenium** (4.6+ recomendado) para automação do navegador
- **Google Chrome** instalado

### Instalação de Dependências

```bash
pip install selenium
```

## 📥 Configuração do WebDriver

1. Baixe o ChromeDriver compatível com sua versão do Chrome em: https://chromedriver.chromium.org/
2. Coloque o arquivo na pasta do projeto ou adicione o caminho ao PATH do sistema

## 🖥️ Como Usar

1. Certifique-se de ter o Chrome instalado e o ChromeDriver no PATH (ou use Selenium 4.6+ para que o Selenium Manager faça o download automático).
2. Execute o script:

```bash
python app.py
```

3. O programa abrirá automaticamente o navegador, coletará os dados e exibirá no terminal.
4. Quando terminar, feche a janela do Chrome (o script não fecha o navegador automaticamente).

## 📊 Dados Coletados

O programa exibe:
- **Data da Coleta**: Data e hora em formato brasileiro
- **Valor Atual de Compra do Dólar**: Cotação para compra
- **Valor Atual de Venda do Dólar**: Cotação para venda
- **Valor Máximo do Dólar (Dia)**: Maior cotação do dia
- **Valor Mínimo do Dólar (Dia)**: Menor cotação do dia

## 🔗 Fonte de Dados

Os dados são coletados do site: https://economia.uol.com.br/cotacoes/cambio/

## ⚙️ Estrutura do Código

- **Importações**: Selenium, manipulação de sistema operacional, controle de tempo
- **Limpar Terminal**: Função que adapta o comando ao SO (Windows/Unix)
- **Inicialização do Driver**: Abre o Chrome e acessa a página
- **Coleta de Dados**: Utiliza seletores CSS para extrair informações específicas
- **Exibição**: Apresenta os dados formatados com data e hora

## 📝 Exemplo de Saída

```
DADOS COLETADOS
DATA DA COLETA: 17/03/2026 14:30

VALOR ATUAL DE COMPRA DO DOLAR: 5.25
VALOR ATUAL DE VENDA DO DOLAR: 5.30
VALOR MAXIMO DO DOLAR (DIA): 5.35
VALOR MINIMO DO DOLAR(DIA): 5.20
```

## ⚠️ Observações Importantes

- O script abre uma janela do Chrome durante a execução
- Certifique-se de ter conexão com a internet
- A página de origem pode sofrer alterações que quebrem os seletores CSS
- Execute o script com permissões apropriadas

## 📄 Licença

Este projeto foi desenvolvido como desafio prático para praticar web scraping com Selenium.

---

**Desenvolvido em Python** | **Utilizando Selenium** | **Web Scraping**
