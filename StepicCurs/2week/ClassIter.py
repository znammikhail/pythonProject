from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

# for i in RandomIterator(10):
#     print(i)

def random_generation(k):
    for i in range(k):
        yield random()

# gen = random_generation(10)

n = int(input())

for i in random_generation(n):
    print(i)

