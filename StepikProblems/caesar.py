n = int(input())
text = str(input().strip())
alfavit = ' abcdefghijklmnopqrstuvwxyz'
new_text = ''
for i in range(len(text)):
    new_text += alfavit[(alfavit.index(text[i]) + n) % len(alfavit)]
print('Result: "{}"'.format(new_text))


