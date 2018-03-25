# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# This code was taken from a youtube video https://youtu.be/Y3n-PA3QoAE on figuring out problem3 on the euler project.
# I had some difficulty with this problem and after viewing the youtube video
# I learned a lot more about coding in python and some key insights in
# how to think about problems. 
# This is the only problem I was not able to complete myself,
# and I put this down to not being familiar enough with Python code.

import math
import logging
logging.basicConfig(level=logging.DEBUG)

def getFactors(number):
        """This function returns the factors of any number"""
        factors = []
        for potentialFactor in range(1,int(math.sqrt(number) + 1)):
            if number % potentialFactor == 0:
                factors.append(potentialFactor)
                factors.append(number // potentialFactor)
        return factors

logging.debug(getFactors(24))

def isPrime(number):
        """This function returns whether the number is prime or not"""
        return (len(getFactors(number)) == 2)

logging.debug('isPrime(24) = %s' % (isPrime(24)))
logging.debug('isPrime(17) = %s' % (isPrime(17)))

allFactors = getFactors(600851475143)
largestPrimefactor = 0
for factor in allFactors:
        if isPrime(factor) and factor > largestPrimefactor:
                largestPrimefactor = factor
print(largestPrimefactor)
