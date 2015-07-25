__author__ = 'Pranavi'

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


def problem_3(x):
    prime_factors = []

    for y in range(2, x):
        if prime_number(y) and x%y ==0:
            prime_factors.append(y)

    print("The largest prime factor of " + str(x) + " is " + str(max(prime_factors)) + ".")


def prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


problem_3(600851475143)