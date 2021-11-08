# import re

# print(re.match.__doc__)
# print(re.search())
# print(re.findall())
# print(re.sub())

# [] - можно указать множество подходящих символов
#  .^$*+?{}[]\|() метасимволы

# pattern = r"a[a,b,c]c"
# string = "dfghabcwdty"
# match_object = re.search(pattern, string)
# print(match_object)
#
# string = 'aac, abc, acc '
# all_inclusion = re.findall(pattern, string)
# print(all_inclusion)
#
# fixed_typos = re.sub(pattern,'abc', string)
# print(fixed_typos)

import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'(\w)\1+'
    print(re.sub(pattern, r'\1', line))

