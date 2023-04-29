from selenium import webdriver as WD
from selenium.webdriver.common.by import By
import pyautogui as PAG
import pandas as PD

# abre o chrome
nav = WD.Chrome()

# abre o site
nav.get('https://www.magazineluiza.com.br/')
produto = input("Digite um produto ")

# Busca o elemento por ID                digita no campo a variavel de input
nav.find_element(By.ID, 'input-search').send_keys(produto)

PAG.sleep(2)
PAG.press('enter')
PAG.sleep(2)

listaProdutos = nav.find_elements(By.CLASS_NAME, 'ejSYWa')
dataFrameList = []
PAG.sleep(2)
for i in listaProdutos:
    nameProduct = ""
    preco = ""
    url = ""

    if nameProduct == "":
        try:
            nameProduct = i.find_element(By.CLASS_NAME, 'hQYVAI').text

        except Exception:
            pass
    elif nameProduct == "":
        try:
            nameProduct = i.find_element(By.CLASS_NAME, 'sc-hFVsQR').text
        except Exception:
            pass

    # -------------

    if preco == "":
        try:
            preco = i.find_element(By.CLASS_NAME, 'bQqJoc').text
        except Exception:
            pass
    elif preco == "":
        try:
            preco = i.find_element(By.CLASS_NAME, 'jDmBNY').text
        except Exception:
            pass
    elif preco == "":
        try:
            preco = i.find_element(By.CLASS_NAME, 'sc-hGglLj').text
        except Exception:
            pass
    elif preco == "":
        try:
            preco = i.find_element(By.CLASS_NAME, 'sc-kDvujY').text
        except Exception:
            pass

    # -----------------
    if url == "":
        try:
            url = i.find_element(By.TAG_NAME, 'a').get_attribute("href")
        except Exception:
            pass
    else:
        url = "-"

    print(f'{nameProduct} - {preco}')
    print(url)

    dados = f'{nameProduct} ; {preco}; {url}'

    dataFrameList.append(dados)

    excel = PD.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
    excel._save()

    dataFrame = PD.DataFrame(dataFrameList, columns=['Nome; Preço; URL'])
    excel = PD.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

    dataFrame.to_excel(excel, sheet_name='Sheet1', index=True)
    excel._save()


