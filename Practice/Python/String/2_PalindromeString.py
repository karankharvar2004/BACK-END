# Check palindrome string

arr = input("Enter Your String: ")

original = arr   
rev = ""

for i in arr:
    rev = i + rev

if original == rev:
    print(original,"is a Palindrome")
else:
    print(original,"is not a palindrome")