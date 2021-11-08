import requests
import re

url1 = input()
url2 = input()


res = requests.get(url1)
if res.status_code == 200:
    pattern = r'a href=[\'"]?([^\'" >]+)'
    string = res.text
    url_arr = re.findall(pattern, string)
    k = 0
    for url in url_arr:
        res = requests.get(url)
        if res.status_code == 200:
            pattern = 'a href=[\'"]?([^\'" >]+)'
            string = res.text
            url_arr = re.findall(pattern, string)
            if url_arr.count(url2) > 0:
                print('Yes')
                k += 1
                break

    if k == 0:
        print('No')





