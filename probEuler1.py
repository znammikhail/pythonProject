sum = 0
n = int(input())
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print (sum)

