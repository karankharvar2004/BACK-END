# LCM Of Two Numbers

def find_lcm(a, b):
    max_num = max(a, b)
    
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM is:", find_lcm(num1, num2))
