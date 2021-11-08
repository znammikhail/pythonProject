import random
koloda = [6,7,8,9,10,2,3,4,11]*4
#print (koloda)
random.shuffle(koloda)
#print (koloda)
print('Поиграем в блекджек ?')
count = 0

while True :
    answer = input("Вы хотите взять карту ?  да или нет \n")
    if answer == "да":
        new_cart = koloda.pop()
        print('Вам попалась карта {}'.format(new_cart))
        count += new_cart
        if count > 21 :
            print('Извините, вы поиграли')
            break
        elif count == 21 :
            print('Вы выиграли!!!')
        else:
            print('У вас {} очков'.format(count))
    elif answer == 'нет':
        print('У вас {} '.format(count))
        break
print('увидимся')





