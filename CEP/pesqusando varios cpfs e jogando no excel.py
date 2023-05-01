from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pyautogui as pg
import pandas as pd

nav = wd.Chrome()
nav.get('https://buscacepinter.correios.com.br/app/endereco/index.php')


pg.sleep(2)

enderecos = {}
dadosDataFrame = []


q = int(input("Quantos CPFs deseja pesquisar? "))



for i in range(q):
    key = i
    value = input("Digite o CPF: ")

    enderecos.update({key:value})


nav.find_element(By.NAME, 'endereco').send_keys('26281070')
pg.sleep(4)

nav.find_element(By.ID, 'btn_pesquisar').click()
pg.sleep(2)



for counter in enderecos.values():
    
    pg.sleep(2)

    nav.find_element(By.ID, 'btn_nbusca').click()

    pg.sleep(2)

    nav.find_element(By.NAME, 'endereco').send_keys(counter)
    pg.sleep(4)

    nav.find_element(By.ID, 'btn_pesquisar').click()
    pg.sleep(2)
    
    tabela = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]')

    endereco = ""
    for L in tabela.find_elements(By.TAG_NAME, 'tr'):
        for C in L.find_elements(By.TAG_NAME, 'td'):
            
            endereco = f'{endereco}; {C.text}'
    dadosDataFrame.append(endereco)
    print(endereco)

excel = pd.ExcelWriter('buscaCep.xlsx', engine='xlsxwriter')
excel._save()

dataFrame = pd.DataFrame(dadosDataFrame, columns=[';Rua;Bairro;Cidade;CEP'])
excel = pd.ExcelWriter('buscaCep.xlsx', engine='xlsxwriter')

dataFrame.to_excel(excel, sheet_name='Dados', index=False)
excel._save()

print("Pronto")