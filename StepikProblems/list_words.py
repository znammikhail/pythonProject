text = input()
spisok = []
spisok = text.split()
new_spisok = []

for i in range(len(spisok)):
    new_spisok.append(len(spisok[i]))
new_spisok.sort()
new_spisok.append(0)
#print(new_spisok)

for i in range(len(new_spisok)-1):
    if new_spisok[i] != new_spisok[i+1]:
        print(str(new_spisok[i]) + ':' + str(new_spisok.count(new_spisok[i])))


