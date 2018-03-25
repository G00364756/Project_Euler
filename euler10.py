# Project Euler - Problem 10
# Aidan O'Connor_G00364756_01/03/2018
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# Please note: This code takes over 5 minutes to run but solves the problem.
# Not efficient!

import math

def Primenumbers(number):
        """This function determines the factors of any number and then returns a list of primes"""
        primes = [1]
        factors = []
        summation = 0
        j = 1
        while primes[-1] < 2000000:
            for a in range(1,(int(math.sqrt(j))+1)):
                if j % a == 0:
                    factors.append(a)
                    factors.append(j//a)
                else:
                    continue
            if len(factors) == 2:
                primes.append(j)
                factors = []
            else:
                factors = []    
            j = j + 1
        trueprimes = []
        for l in primes: 
            if l not in trueprimes and l < 2000000: # creates a new list that takes away all the duplicates from the original list
                trueprimes.append(l)
        summation = sum(trueprimes)-1
        return(summation)

ans = Primenumbers(1)
print(ans)

