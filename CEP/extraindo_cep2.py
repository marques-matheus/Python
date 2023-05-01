from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pyautogui as pg
import pandas as pd

nav = wd.Chrome()
nav.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

cep = input("Digite seu cep: ")

pg.sleep(2)
nav.find_element(By.NAME, 'endereco').send_keys(cep)
pg.sleep(4)

nav.find_element(By.ID, 'btn_pesquisar').click()
pg.sleep(2)

dados = []

tabela = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')


for L in tabela.find_elements(By.TAG_NAME, 'tr'):
    endereco = ""
    for C in L.find_elements(By.TAG_NAME, 'td'):

        endereco = f'{endereco}; {C.text}'

dados.append(endereco)

excel = pd.ExcelWriter('dadoscep.xlsx', engine='xlsxwriter')
excel._save()

dataFrame = pd.DataFrame(dados, columns=['Dados'])
excel = pd.ExcelWriter('dadoscep.xlsx', engine='xlsxwriter')

dataFrame.to_excel(excel, sheet_name='Sheet1', index=True)
excel._save()


input("")