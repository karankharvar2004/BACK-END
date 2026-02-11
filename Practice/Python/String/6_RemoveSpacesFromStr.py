# Remove spaces from string

str = input("Enter Your String: ")

new_str = ""

for i in str:
    if i.replace(" ",""):
        new_str += i

print(new_str)

# for i in str:
#     if i != " ":
#         new_str += i

# print(new_str)