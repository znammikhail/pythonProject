
with open('texts/dataset_24465_4.txt', 'r') as f, open('texts/text_revers', 'w') as w:
    a = []
    for line in f:
        a.append(line.strip())
    print(a)
    a.reverse()
    str = ''
    str = '\n'.join(a)
    w.write(str)
