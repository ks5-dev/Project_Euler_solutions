#the function for generating pythagoreanTriplets is from GeeksForGeeks
def pythagoreanTriplets(limits) :
    res = []
    c, m = 0, 2

    while c < limits :

        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limits :
                break
            res.append([a,b,c])
        m = m + 1
    return res

def pro(arr):
    sum = 1
    for i in arr:
        sum *= i
    return sum

triplets = pythagoreanTriplets(1000)
for i in range(len(triplets)-1):
    if sum(triplets[i]) == 1000:
        print(pro(triplets[i]))
