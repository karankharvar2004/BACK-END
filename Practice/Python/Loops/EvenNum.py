num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Even numbers between", int(num1), "and", int(num2), "are:")

for i in range(int(num1), int(num2)):
    if i % 2 == 0:
        print(i)