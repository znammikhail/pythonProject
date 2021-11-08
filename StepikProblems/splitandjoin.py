chisla = input().split()
x = input()
count = 0

for i in range(len(chisla)):
    if chisla[i] == x:
        print(i, end=' ')
        count += 1
if count == 0:
    print('None')



