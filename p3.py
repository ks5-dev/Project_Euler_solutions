from utils.check_prime import CheckPrime

#this will work, but takes a long amount of time
def find_largest(n):
    prime_factors = []
    for i in range(2,n//2+1):
        if n%i == 0:
            if CheckPrime(i):
                prime_factors.append(i)
    return prime_factors

def find_largest_generator(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            if CheckPrime(i):
                print(i)
                yield i
print(max(list(find_largest_generator(600851475143))))
#see the last output, that is the result
