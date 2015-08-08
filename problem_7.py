__author__ = 'Pranavi'

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

import math

def problem_7(x): #x is the xth prime number
    i = 0
    prime_iterator = 0
    num = 0

    while prime_iterator <= x:
        i += 1
        if is_prime(i):
            prime_iterator += 1
            if prime_iterator == x:
                num = i
                break

    print("The #" + str(x) + " prime number is " + str(num) + ".")

def is_prime(x):    #checks if the integer is prime
    if x == 2:
        return True
    elif x % 2 == 0 or x == 1:
        return False
    else:
        for i in range(3, (int(round(math.sqrt(x)))) + 1, 2):
            if x % i == 0:
                return False
        else:
            return True

problem_7(6)
problem_7(10001)