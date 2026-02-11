# Print even numbers between 1 to N

num = int(input("Enter Your Number: "))

# Using FOR Loop

for i in range(0, num+1):
    if i % 2 == 0:
        print(i)



# Using WHILE Loop

# i = 1
# while i <= num:
#     if i % 2 == 0:
#         print(i)
#     i += 1