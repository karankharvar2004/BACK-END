# Check palindrome number

num = int(input("Enter Your Number: "))

original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print(original ,"is a Palindrome")
else:
    print(original ,"is not a Palindrome")