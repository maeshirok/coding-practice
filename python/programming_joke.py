"""
Joke APIを利用してプログラミングに関するジョークをいうコードです。
"""
import requests

url = "https://official-joke-api.appspot.com/jokes"
endpoint = "/programming/random"
url = url + endpoint

responce = requests.get(url)
r = responce.json()

print(r[0]['setup'])
print(r[0]['punchline'])