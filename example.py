import requests
import json
from forex_python.converter import CurrencyRates
import os

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR') 
print(rate)

litecoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
response = requests.get(litecoin_api_url)
response_json = response.json()
print(response_json)

for coin in response.json():
    price = coin.get("price_usd", "U$S Price not provided")
    litecoin_price = float(("{0:.2f}").format(float(price)))
    print("$ " + str(litecoin_price))
    litecoin_price_eur = float(("{0:.2f}").format(float(price)*rate))   
    print("€ " + str(litecoin_price_eur))
