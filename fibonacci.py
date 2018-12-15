def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n < 1:
        print("You cannot enter negative numbers")
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


while True:
    f = int(input("Enter a positive integer "))
    print(fibonacci(f))
