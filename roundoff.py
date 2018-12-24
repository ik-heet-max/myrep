def round_off():
    a = float(input("Введите число: "))
    b = a//1 + 0.5
    if a >= b:
        c = b + 0.5
    else:
        c = b - 0.5
    return c

print(round_off())