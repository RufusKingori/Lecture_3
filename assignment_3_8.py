#program so that it finds the sum and also the average of the 5 numbers.
def main():

    a, b, c, d, e = eval(input("Enter five whole numbers: "))

    sum = 0

    list = [a, b, c, d, e]

    for i in range(0, len(list)):

        sum = sum + i
        average = sum/len(list)

    print("The sum of the five numbers is: ", sum)

    print("The average of the five numbers is: ", average)

main()