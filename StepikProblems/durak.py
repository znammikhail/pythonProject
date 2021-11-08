First, Second = input().split()
kozir = str(input())
koloda = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
masti = ['C', 'D', 'H', 'S']


if First[1] == Second[1]:
    if koloda.index(First[0]) > koloda.index(Second[0]):
        print('First')
    else :
        print('Second')
elif First[1] == kozir:
    print('First')
elif Second[1] == kozir:
    print('Second')
else:
    print('Error')

