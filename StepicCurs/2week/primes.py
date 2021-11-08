import itertools

def primes():
    a = 1
    while True:
        count: int = 1
        a += 1
        for i in range(2, a):
            if a % i == 0:
                count += 1
        if count == 1:
            yield a

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
