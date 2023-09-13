'''
2023/08/07
Joke APIを利用してプログラミングに関するジョークを出力
'''
import requests

url = 'https://official-joke-api.appspot.com/jokes'
endpoint = '/programming/random'
url = url + endpoint

responce = requests.get(url)
r = responce.json()

print(f'setup:{r[0]["setup"]}')
print(f'punchline:{r[0]["punchline"]}')