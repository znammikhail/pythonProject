import collections
words = input().lower().split()
c = collections.Counter()
for word in words:
    c[word] += 1
for key in c.keys():
    print('{} {}'.format(key,c.get(key)))
