# Print Inverted left-angled triangle

num = int(input("Enter Size: "))

for i in range(num,0,-1):

    for j in range(num - i):
        print("  ", end="")

    for j in range(i):
        print("* ", end="")

    print()
