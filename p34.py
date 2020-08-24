from utils.factorial import Factorial
def check(n):
    digits = [int(i) for i in str(n)]
    sum = 0
    for digit in digits:
        sum += Factorial(digit)
    return sum == n

def main():
    sum = 0
    for i in range(3,100000):
        if check(i):
            sum += i
    print(sum)

main()
