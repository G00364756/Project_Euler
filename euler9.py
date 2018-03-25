# Project Euler - Problem 9
# Aidan O'Connor_G00364756_01/03/2018
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def Ptriplet(number):
    """Returns the Pythagorean triplet for which a + b + c = 1000"""
    m = 3
    limit = 1000
    for a in range(m,500,1):
        for b in range(a,500,1):
            for c in range (b,500,1):
                ram = a + b + c
                zig = a**2
                zag = b**2
                zigzag = zig + zag
                bag = c**2
                if ram == limit and zigzag == bag and a < b:
                    return (a, b, c)

ans = Ptriplet(1)
print(ans)