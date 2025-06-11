def factorial (n :int):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number : "))
print("Factorial of", num, "is:",factorial(num))