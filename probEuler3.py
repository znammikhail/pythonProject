# простые делители

num = int(input())
#answer = []
delitel = 2
while delitel*delitel <= num:
    if num % delitel == 0:
        #answer.append(delitel)
        num = num // delitel
    else:
        delitel += 1
print(num)
#answer.append(num)
#print(answer)
#print(max(answer))

