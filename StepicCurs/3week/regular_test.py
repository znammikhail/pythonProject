import re

pattern = r"a[ab]+?a"  # ? делает не жадный метод (ищет короткую строку)
string = 'abaaba'

print(re.match(pattern, string))
print(re.findall(pattern, string))

