from utils.sum_of_digit import SumDigit
import itertools
def generate_power_of_2():
    res = 2
    for i in range(2,1001):
        yield pow(res,i)

index = 998
print(SumDigit(next(itertools.islice(generate_power_of_2(), index, None))))
