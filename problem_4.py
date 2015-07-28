__author__ = 'Pranavi'

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def problem_4():
    largest_palindrome = 0
    prev_palindrome = 0

    for x in range(999, 100, -1):
        for y in range(x, 100, -1):
            if is_palindrome(x, y):
                prev_palindrome = x * y
                if prev_palindrome > largest_palindrome:
                    largest_palindrome = prev_palindrome

    print(str(largest_palindrome))


def is_palindrome(x, y):
    pal_sum = x * y
    digits = list(str(pal_sum))
    opposite_digits = list(digits)
    opposite_digits.reverse()

    if digits == opposite_digits:
        return True
    else:
        return False


problem_4()
