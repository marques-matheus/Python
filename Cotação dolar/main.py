import requests
import schedule
import time
import datetime

def check_dollar():
   
    tempo = datetime.datetime.now().strftime("%H:%M:%S")
    response = requests.get('https://economia.awesomeapi.com.br/json/USD')
    data = response.json()
    cotacao = data[0]['ask']
    print(f'A cotação atual do dólar é R$ {cotacao} | Verificado em: {tempo}')


check_dollar()
schedule.every(30).minutes.do(check_dollar)

while True:
    schedule.run_pending()
    time.sleep(1)