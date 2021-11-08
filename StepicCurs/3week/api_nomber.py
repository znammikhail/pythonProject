import sys
import requests

for line in sys.stdin:
    number = line.rstrip()
    api_url = 'http://numbersapi.com/{}/math?json=true'.format(number)

    res = requests.get(api_url)
    # print(res.status_code)
    # print(res.headers['Content-type'])
    if res.json()['found']:
        print('Interesting')
    else:
        print('Boring')

