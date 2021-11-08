s = input()
a = input()
b = input()
i = 0
while s.find(a) != -1 and i < 1000:
    i += 1
    s = s.replace(a, b)

if i == -1 or i >= 1000:
    print('Impossible')
else:
    print(i)
