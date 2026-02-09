# Print Pyramid Pattern

num = int(input("Enter Size: "))

for i in range(1, num + 1):
    
    # Print spaces
    for j in range(num - i):
        print("  ", end="")
    
    # Print stars
    for j in range(2 * i - 1):
        print("* ", end="")
    
    print()


# for i in range(1, num + 1):
#     print("  " * (num - i) + "* " * (2*i - 1))