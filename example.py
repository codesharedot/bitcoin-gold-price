import requests
import json
from forex_python.converter import CurrencyRates
import os

c = CurrencyRates()
rate = c.get_rate('USD', 'EUR') 
print(rate)

ripple_api_url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'
response = requests.get(ripple_api_url)
response_json = response.json()
print(response_json)

for coin in response.json():
    price = coin.get("price_usd", "U$S Price not provided")
    ripple_price = float(("{0:.2f}").format(float(price)))
    print("$ " + str(ripple_price))
    ripple_price_eur = float(("{0:.2f}").format(float(price)*rate))   
    print("€ " + str(ripple_price_eur))
