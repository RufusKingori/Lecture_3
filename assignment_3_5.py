#This function computes the

def main():
    n = int(input("Please enter a whole number: "))
    fact = 1

    for factor in range(1, n+1):
        fact = fact * 5

    print("The factorial of", n, "is", fact)

main()