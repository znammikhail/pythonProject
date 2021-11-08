import simplecrypt

with open("texts/encrypted.bin", "rb") as inp:
    encrypted = inp.read()

password = open("texts/passwords.txt", "r")
lines = password.readlines()
password.close()
print(lines)

for line in lines:
    try:
        a = simplecrypt.decrypt(line.strip(), encrypted)
    except simplecrypt.DecryptionException:
        print('пароль {} не подходит'.format(line.strip()))

print(a)






