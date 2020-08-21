def main():
    fibonanci = [1,1,2,3]
    a = 1 
    b = 2 
    c = a+b 
    while len(str(c)) < 1000:
        a = b
        b = c
        c = a+b
        fibonanci.append(c)
    return len(fibonanci)
print(main())