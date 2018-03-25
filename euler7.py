# Project Euler - Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def Primenumbers(number):
        """This function returns the factors of any number"""
        primes = []
        factors = []
        j = 1
        while len(primes) < 10002:
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
        i = primes[-1]
        return(i)

ans = Primenumbers(1)
print(ans)

