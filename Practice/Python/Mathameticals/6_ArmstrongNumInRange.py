# Print Armstrong Number in Range

def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0
    
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    
    return total == num

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Armstrong numbers in range:")

for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)
