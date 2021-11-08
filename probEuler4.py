#число полиндром
c = 1
count = 0
for a in range(100,999):
    for b in range(100,999):
        c = a*b
        rev_c = str(c)[::-1]
        if str(c) == rev_c  and c > count:
            count = c
print(count)
