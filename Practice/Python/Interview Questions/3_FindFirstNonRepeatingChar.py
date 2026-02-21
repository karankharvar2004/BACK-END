# Find First Non-Repeating Character

str = input("Enter Your String: ")

for i in range(len(str)):
    count = 0

    for j in range(len(str)):
        if str[i] == str[j]:
            count += 1

    if count == 1:
        print("First Non-Repeating Character is: ",str[i])


# Find multiple Non-Repeating Character

# str = input("Enter Your String: ").lower()

# for i in range(len(str)):

#     if str[i] == " ":
#         continue

#     count = 0

#     for j in range(len(str)):
#         if str[i] == str[j]:
#             count += 1 

#     if count == 1:
#         print("First Non-Repeating Character is: ",str[i])


