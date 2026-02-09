# Print right-angled triangle

num = int(input("Enter Size: "))

for i in range(1, num+1):
    for j in range(i):
        print("* ",end="")
    print()