from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pyautogui as pg

nav = wd.Chrome()
nav.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

cep = input("Digite seu cep: ")

pg.sleep(2)
nav.find_element(By.NAME, 'endereco').send_keys(cep)
pg.sleep(4)

nav.find_element(By.ID, 'btn_pesquisar').click()
pg.sleep(2)

rua = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
print(f'Rua: {rua}')

bairro = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
print(f'Bairro: {bairro}')

localidade = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
print(f'Cidade: {localidade}')

cepR = nav.find_element(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text
print(f'CEP: {cepR}')



input("")