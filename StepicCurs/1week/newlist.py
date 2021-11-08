objects = [1, 2, 1, 2, 3]


def new_list(objects):
    newlist = []
    for i in objects:
        if i not in newlist:
            newlist.append(i)
    return newlist

print(new_list(objects))
