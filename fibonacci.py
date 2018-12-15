def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))
