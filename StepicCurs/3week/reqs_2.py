import requests
import re

res = input()
# res = requests.get(html)
# if res.status_code == 200:
pattern = r'<a []+ href=[\'"]?([^\'" >]+)'
# string = res.text
url_arr = re.findall(pattern, res)
print(url_arr)
url_arr.sort()
# for url in url_arr:
#     print(url)

