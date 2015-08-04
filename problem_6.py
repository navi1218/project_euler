__author__ = 'Pranavi'

'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def problem_6():
    sum = 0
    square_of_sum = 0

    for i in range(1, 101):
        sum += i
        square_of_sum += i * i

    difference = (sum * sum) - square_of_sum

    print("The difference between the sum of of the squares of the first 100 natural numbers and the square of the sum is " + str(difference) + ".")

problem_6()
