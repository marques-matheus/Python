from selenium import webdriver as opcoesNav
from selenium.webdriver.common.by import By

#abre o chrome
nav = opcoesNav.Chrome()

#acessa o site
nav.get('https://rpachallengeocr.azurewebsites.net/')

#Acha o elemento peo XPATh
elementTable = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]')


#percorre linhas e colunas
linhas = elementTable.find_elements(By.TAG_NAME, 'tr')
colunas = elementTable.find_elements(By.TAG_NAME, 'td')

#contador de linhas
linha = 1


#Para cada linha na variavel linha, imprime a linha atual e adiciona +1 no contador
for L in linhas:
    print(L.text)
    linha += 1

input("Pressione qualquer tecla para fechar o navegador")
nav.quit()