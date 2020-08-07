from utils.check_prime import CheckPrime
import itertools
import sys

def generate_primes():
    while True:
        for i in range(1,sys.maxsize):
            if CheckPrime(i):
                yield i

#tips : this is how you can get a nth element from a generator
index = 10001
print(next(itertools.islice(generate_primes(), index, None)))
