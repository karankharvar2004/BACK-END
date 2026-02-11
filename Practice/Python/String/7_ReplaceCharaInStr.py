# Replace character in string

str = input("Enter Your String: ")

old_char = input("Enter Your Old Character: ")
new_char = input("Enter Your New Character: ")

new_str = ""

for i in str:
    if i != "":
        if i == old_char:
            new_str += new_char
        else:
            new_str += i  

print(new_str)