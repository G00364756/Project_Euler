# Project Euler - Problem 11
# Aidan O'Connor_G00364756_01/03/2018
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import fileinput


input_file = 'euler11.csv'
output = open('out.txt', 'w+')

with open('out.txt', 'w+') as output:
    for each_line in fileinput.input(input_file):
        output.write("\n".join(x.strip() for x in each_line.split(',')))
