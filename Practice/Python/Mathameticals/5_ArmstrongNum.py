# Check For a Armstrong Number

def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    
    return total == num

num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
