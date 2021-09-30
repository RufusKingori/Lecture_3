#This program computes the square root of a number.
#The program uses a function from the math library.

import math

def main():
    number = int(input("Enter a number to compute it's square root: "))

    number_sqr = math.sqrt(number)

    print("The square root of the number is:", number_sqr)

main()