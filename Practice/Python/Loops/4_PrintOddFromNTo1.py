# Print odd numbers between N to 1

num = int(input("Enter Your Number: "))

# Using FOR Loop

for i in range(num,0,-1):
    if i % 2 != 0:
        print(i)



# Using WHILE Loop

# i = num
# while i >= 0:
#     if i % 2 != 0:
#         print(i)
#     i -= 1