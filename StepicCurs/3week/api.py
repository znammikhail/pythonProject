
import requests

city = input("City? ")
api_url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,  # Saint Petersburg
    'appid': 'da22962c5b77cb0eacb8c01e9e4435f9',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-type'])
# print(res.json())

data = res.json()
temlate = 'Corrent temperature in {} is {}'
print(temlate.format(city, data['main']['temp']))
