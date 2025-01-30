def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print("The factorial of ",n," is:",fact(n))
