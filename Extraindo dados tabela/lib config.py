from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By

navegador = opcoesSelenium.Chrome()

navegador.get('https://globo.com')

input("Pressione qualquer tecla para fechar o navegador")

navegador.quit()