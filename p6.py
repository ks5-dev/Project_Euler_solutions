def find_difference(a,b):
    #sum of the square
    sum_square = 0
    for i in range(a,b+1):
        sum_square += i*i
    #square of the sum
    square_sum = 0
    for i in range(a,b+1):
        square_sum += i
    square_sum = square_sum * square_sum

    return square_sum - sum_square

print(find_difference(1,100))
