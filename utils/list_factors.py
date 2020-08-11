def ProperDivisor(n):
    result = []
    for i in range(1,n//2+1):
        if n%i == 0:
            result.append(i)
    return result

'''
The difference is that the first function doesn't contain n, whereas the second one does
'''

def ListFactor(n):
    result = []
    for i in range(1,n//2+1):
        if n%i == 0:
            result.append(i)
    result.append(n)
    return result
