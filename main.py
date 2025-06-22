import requests

r = requests.get('https://lolalytics.com/lol/kayle/build/')

print(r.text)