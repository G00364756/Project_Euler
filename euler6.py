#Euler Project - Problem 6
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumsquare(number):
    num = 0
    for a in range (0,101,1):
            b = a**2
            num = num + b
    return(num)

def squaresum(number):
    d = 0
    for c in range (0,101,1):
        d = d + c
    e = d**2
    return (e)

ans = squaresum(1)-sumsquare(1)
print(ans)
