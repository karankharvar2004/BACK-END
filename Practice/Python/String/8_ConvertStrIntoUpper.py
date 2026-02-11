# Convert string to uppercase/lowercase (without built-in)

str = input("Enter Your String: ")

upper_str = ""
lower_str = ""

for i in str:
    # For uppercase
    if 'a' <= i <= 'z':
        upper_str += chr(ord(i) - 32)
    else:
        upper_str += i
    
    # For lowercase
    if 'A' <= i <= 'Z':
        lower_str += chr(ord(i) + 32)
    else: 
        lower_str += i

print("Uppercase:", upper_str)
print("Lowercase:", lower_str)