
## Automação na qual preenche informações em um site (fictício) através de informações dentro de uma planilha

# Realizar as importações das bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

# 1 - Navegar até o site: https://contabilidade-devaprender.netlify.app/
driver = webdriver.Chrome()
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

# 2 - Digitar e-mail
email = driver.find_element(By.XPATH,"//input[@id='email']") #XPATH --> tag[@atributo='valor']
sleep(2)
email.send_keys('admin@contabilidade.com')

# 3 - Digitar a senha
senha = driver.find_element(By.XPATH,"//input[@id='senha']")
sleep(2)
senha.send_keys('Contabil1234')

# 4 - Clicar em "Entrar"
botao_entrar = driver.find_element(By.XPATH,"//button[@id='Entrar']")
sleep(2)
botao_entrar.click()
sleep(8)

# 5 - Extrair informações da planilha
empresas = openpyxl.load_workbook('C://Users/jamil/OneDrive/Área de Trabalho/Desafios - Python/Projetos/Automação/Automação - Site e planilha/empresas.xlsx')
pagina_empresas = empresas['dados empresas']

# 6 - Clicar em cada campo e preencher com a informação extraída da planilha
for linha in pagina_empresas.iter_rows(min_row=2, values_only=True): # Values_only --> para realizar o Unpacking, o que seria "guardar" cada informação da planilha em uma variável
    nome_empresa, email1, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_fundacao = linha

    driver.find_element(By.ID,'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,'emailEmpresa').send_keys(email1)
    sleep(1)
    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID,'dataFundacao').send_keys(data_fundacao)
    sleep(1)

# 7 - Clicar em "Cadastrar"
    botao_cadastrar = driver.find_element(By.XPATH,"//button[@id='Cadastrar']")
    sleep(1)
    botao_cadastrar.click()
    sleep(5)

# 8 - Programa irá repetir passo 6 e 7 até terminar os dados da planilha