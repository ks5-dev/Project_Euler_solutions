from utils.factorial import Factorial
import itertools
def generate():
    for i in str(Factorial(100)):
        yield int(i)

def find():
    sum = 0
    for i in range(150): #I actually choose a number between 100 and 200 to see what is the last value this can return
        sum += next(itertools.islice(generate(),i, None))
    return sum
print(find())
