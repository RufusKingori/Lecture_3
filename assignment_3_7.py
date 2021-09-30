#This program inputs 5 numbers from the user in a loop and finds the sum of the numbers.

def main():

    a, b, c, d, e = eval(input("Enter five whole numbers: "))

    sum = 0

    list = [a, b, c, d, e]

    for i in range(0, len(list)):

        sum = sum + i

    print("The sum of the five numbers is:", sum)

main()