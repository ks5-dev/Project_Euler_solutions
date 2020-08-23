import string
words=[]

seq = []
def triangle_seq():
    for i in range(40):
        seq.append(int(1/2*i*(i+1)))
triangle_seq()

def main():
    count = 0
    for i in words :
        sum = 0
        for j in i :
            sum += string.ascii_lowercase.index(j.lower())+1
        if sum in seq:
            count += 1
            print(sum)
    return count

print(main())
