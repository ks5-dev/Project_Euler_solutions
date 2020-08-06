def find_sum(limit):
    even_fibonacci = [2] # first even fibonacci numbers
    a = 1 #first term
    b = 2 # second term
    c = a+b # next term
    while c < limit:
        a = b
        b = c
        c = a+b
        if c%2 == 0:
            even_fibonacci.append(c)
    return sum(even_fibonacci)

print(find_sum(4000000))
