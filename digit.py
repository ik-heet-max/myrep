n = int(input("Enter an integer "))
num = []
while n > 1:
    a = n % 10
    n = n // 10
    num.append(a)
print("The largest digit in the number entered is", max(num))