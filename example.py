import requests
import json
from forex_python.converter import CurrencyRates
import os

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR') 
print(rate)

huobi-token_api_url = 'https://api.coinmarketcap.com/v1/ticker/huobi-token/'
response = requests.get(huobi-token_api_url)
response_json = response.json()
print(response_json)

for coin in response.json():
    price = coin.get("price_usd", "U$S Price not provided")
    coin_price = float(("{0:.2f}").format(float(price)))
    print("$ " + str(coin_price))
    coin_price_eur = float(("{0:.2f}").format(float(price)*rate))   
    print("€ " + str(coin_price_eur))
