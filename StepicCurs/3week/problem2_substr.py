s = input()
t = input()
a = []
count = 0

for i in range(len(s)-len(t)+1):
    if s.find(t, i) != -1:
        if s.find(t, i) is not a:
            a.append(s.find(t, i))

print(len(set(a)))
