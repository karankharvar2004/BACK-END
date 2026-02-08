# Simple calculator using if-else

num1 = float(input("Enter your 1st Num: "))
operator = input("Enter your choice from ( + - * / ): " )
num2 = float(input("Enter your 2nd Num: "))

if operator == "+":
    print("Result: ",num1 + num2)

elif operator == "-":
    print("Result: ",num1 - num2)

elif operator == "*":
    print("Result: ",num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result: ",num1 / num2)
    else:
        print("Error: Division by zero not allowed")
else:
    print("Invalid Operator, Choose correct Operator!!")



