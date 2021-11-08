# число которое делится без остатка на все от 1 до 20

def min_num(n) :
    '''Нахождение всех простых до n'''
    mul = []
    for a in range(1,n+1):
        i = 0
        for b in range(1,n+1):
            if a % b == 0:
                i += 1
        if i == 2:
            mul.append(a)
    print(mul)

a = int(input('Vvedite chislo '))
min_num(a)



