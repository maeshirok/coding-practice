"""
CoinGecko APIを利用してbitcoinの価格を取得するプログラムです。
"""
import requests
  
url = "https://api.coingecko.com/api/v3"
endpoint = "/simple/price"
url = url + endpoint
params = {"ids":"bitcoin","vs_currencies":"jpy,usd"}

response = requests.get(url, params=params)
r = response.json()

print("1BTCの価格")
print(str(r['bitcoin']['jpy']) + "円")
print(str(r['bitcoin']['usd']) + "ドル")