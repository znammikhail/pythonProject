class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        else:
            super(PositiveList, self).append(x)


a = PositiveList()
a.append(-4)
print(a)
