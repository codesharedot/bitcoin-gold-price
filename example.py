import requests
import json
from forex_python.converter import CurrencyRates
import os

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR') 
print(rate)

ethereum_api_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
response = requests.get(ethereum_api_url)
response_json = response.json()
print(response_json)

for coin in response.json():
    price = coin.get("price_usd", "U$S Price not provided")
    ethereum_price = float(("{0:.2f}").format(float(price)))
    print("$ " + str(ethereum_price))
    ethereum_price_eur = float(("{0:.2f}").format(float(price)*rate))   
    print("€ " + str(ethereum_price_eur))
