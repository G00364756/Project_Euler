# Aidan O'Connor - G00364756 - 22/02/2018
# Project Euler_Problem 5:
# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

# This code is cumbersome and inefficient but gets the job done.
# I imagine the aim of the exercise is to become more capable with 
# loops, ranges and lists but I wanted to see if I could 
# intuitively create code to solve this problem rather than googling
# how to do it.

# I originally set n to 1 and incremented n by 1 but this took
# over 30 seconds to compute. Setting n to 20 as the starting point, 
# because the range of numbers that we have to divide by ends at 20, 
# and incrimenting by 20 speeds the code up drastically without
# comprimising what the code is intended to do.

# Set n greater than 0 as zero modulus anything gives a remainder of 0.
n = 20
# This is where the code could encounter problems, if the
# end result is a larger than the number we set the loop limit to
# the code will never reach the end result. Need to put in a very large number
# to account for this, or in this case set the loop to something it will
# never reach ( i.e. while n is not equal to zero "n != 0")
# The improvements mean the code spits out the final value in 5 seconds.

while n != 0:
    # I wasn't sure how to do the modulus operand with arrays so I had
    # to list the criteria individually and link them with and "and"
    # operand.
    if  (n % 1 == 0) and (n % 2 == 0) and (n % 3 == 0) and (n % 4 == 0) and (n % 5 == 0) and (n % 6 == 0) and (n % 7 == 0) and (n % 8 == 0) and (n % 9 == 0) and (n % 10 == 0) and (n % 11 == 0) and (n % 12 == 0) and (n % 13 == 0) and (n % 14 == 0) and (n % 15 == 0) and (n % 16 == 0) and (n % 17 == 0) and (n % 18 == 0) and (n % 19 == 0) and (n % 20 == 0):
        print(n)
        break
        # It is important to use break otherwise the code will continue
        # to spit out the final value, an endless loop.
    else:
        n = n + 20

