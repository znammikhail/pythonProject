# print('1234'.find('123'))
# print(int('101101', base=4))

# print(str.find.__doc__)

# s = 'abacaba'

# print (s.startswith('qw'))
# print(s.endswith('.txt'))

# print(s.find('aba'))
# print(s.rfind('aba'))

# print(str.split.__doc__)

import requests
template = 'Response from {0.url} with code {0.status_code}'

res = requests.get('http://docs.python.org/3.5/')
print(template.format(res))

res = requests.get('http://docs.python.org/3.5/random')
print(template.format(res))