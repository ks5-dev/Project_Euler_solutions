def CheckPrime(n):
    result = True
    for i in range(2,n//2):
        if n%i == 0:
            result = False
            break
    return result
