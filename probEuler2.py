#Fibonachi
n = 4000000
sum = 2
a = 1
b = 2
while b < n:
    b += a  # чтобы не использовать третью переменную
    a = b - a
    if b % 2 == 0:
        sum += b
print(sum)