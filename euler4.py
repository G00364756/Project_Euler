# Aidan O'Connor - Project Euler (Problem 4) 
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


n = 0
Alps = []
for a in range(999, 0, -1):
    for b in range(a, 0, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                 Alps.append(x)
                 answer=max(Alps)
print (answer)