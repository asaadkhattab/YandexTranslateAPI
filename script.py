import requests

API_KEY = 'trnsl.1.1.20200510T212315Z.6e3b997c11482427.15d523e425bd9106df55174cb4e7d4e932ad7d1b'

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



params = dict(key=API_KEY, text='Good', lang='en-ar')

res = requests.get(url, params=params)

print(res.text)

print(res.status_code)