def divisible(n,arr):
    tmp = 0
    for i in arr:
        if n% i ==0:
            tmp += 1
    return tmp == len(arr)
#print(divisible(2520,[1,2,3,4,5,6,7,8,9,10])) --> True

def find_smallest(a,b):
    tmp = 2
    while True:
        result = b*tmp
        if divisible(result,[i for i in range(a,b+1)]):
            return result
            break
        tmp += 1

print(find_smallest(1,20))
#the answer is long and might take a long time to find
