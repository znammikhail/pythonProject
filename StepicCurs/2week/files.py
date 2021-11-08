
f = open('texts/text.txt', 'r')

x = f.read().split()
# for line in f:
#     print(line.split())

f.close()

x.sort()

print('\n'.join(x))