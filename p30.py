import itertools
def check(n):
    result = 0
    num = [int(i) for i in str(n)]
    for i in num :
        result += i*i*i*i*i
    return result == n

def generate():
    lst = []
    for i in range(2,1000000):
        if check(i):
            lst.append(i)
    return lst

def main():
    return sum(generate())
print(main())
'''
'''
