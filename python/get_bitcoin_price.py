"""
2023/08/11
CoinGecko APIを利用してbitcoinの価格を取得し出力
"""
import requests

url = "https://api.coingecko.com/api/v3"
endpoint = "/simple/price"
url = url + endpoint
params = {"ids":"bitcoin","vs_currencies":"jpy,usd"}

response = requests.get(url, params=params)
r = response.json()

jpy = '{:,}'.format(r['bitcoin']['jpy'])
usd = '{:,}'.format(r['bitcoin']['usd'])

print(f"{jpy} JPY")
print(f"{usd} USD")