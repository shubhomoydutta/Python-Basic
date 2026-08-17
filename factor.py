num = int(input("Enter a number: "))

fact = 1
i = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    while i <= num:
        fact = fact * i
        i = i + 1
    print("The factorial of", num, "is", fact)

