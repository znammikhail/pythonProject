
def happytiket():
    f = open('text.txt', 'w')
    count = 0
    lis = []
    for i in range(100000, 1000000):
        left = i % 1000
        right = i // 1000
        if  (left % 10) + (left % 100 // 10) + (left // 100) == (right % 10) + (right % 100 // 10) + (right // 100)  :
            count += 1
            lis.append(i)
    count = count / 900000 * 100
    f.write(str(count) + "шестизначных счатливых билетов \n")
    for i in lis:
        f.write(str(i) + '\n')

happytiket()