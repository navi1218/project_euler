__author__ = 'Pranavi'

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def problem_1():
    sum_3 = 0
    for x in range(1, 1000):
        if x % 3 == 0:
            sum_3 += x  # sum of all multiples of 3 below 1000

    sum_5 = 0
    for y in range(1, 1000):
        if y % 5 == 0:
            sum_5 += y  # sum of all multiples of 5 below 1000

    intersect_3and5 = 0
    for z in range (1,1000):
        if (z % 5 == 0 and z % 3 == 0):
            intersect_3and5 += z

    print("The sum of all the multiples of 3 or 5 below 1000 is " + str(sum_3+sum_5-intersect_3and5) + ".")

problem_1()