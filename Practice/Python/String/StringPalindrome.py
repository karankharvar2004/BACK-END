s = input("Enter Your String: ")
rev = ""

for i in s:
    rev = i + rev

print("Reversed String:",rev)


if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")