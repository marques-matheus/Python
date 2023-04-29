from selenium import webdriver as opcoesNav
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui as pg

#abre o chrome
nav = opcoesNav.Chrome()

#acessa o site
nav.get('https://rpachallengeocr.azurewebsites.net/')


#Lista para salvar os dados
frame = []

#contador de linhas
linha = 1

#variavel contadora do while
i = 1

while i < 4:

    # Acha o elemento peo XPATh
    elementTable = nav.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # percorre linhas e colunas
    linhas = elementTable.find_elements(By.TAG_NAME, 'tr')
    colunas = elementTable.find_elements(By.TAG_NAME, 'td')

    for L in linhas:
        print(L.text)
        #append = push - insere os dados em forma de texto na lista
        frame.append(L.text)
        linha += 1

    #adiciona +1 no contador do while
    i += 1

    pg.sleep(2)

    #dentro do while, acha o botão de next e clica
    nav.find_element(By.XPATH,  '//*[@id="tableSandbox_next"]').click()

    pg.sleep(2)

else:
    print('Pronto')


#define o nome do arquivo do excel e o engine
excel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
#salva o arquivo em branco
excel._save()

#usa a lista para salvar os dados no excel
dataFrame = pd.DataFrame(frame, columns=['Dados'])
excel = pd.ExcelWriter('dadosSite.xlsx', engine='xlsxwriter')
#seleciona a tabela para salvar
dataFrame.to_excel(excel, sheet_name='Sheet1', index=True)
#salva os dados
excel._save()


input("Pressione qualquer tecla para fechar o navegador")
