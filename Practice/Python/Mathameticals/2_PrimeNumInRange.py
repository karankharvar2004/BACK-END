#  Print prime numbers in a range

num = int(input("Enter Size: "))

count = 0

for i in range(1,num):
    for j in range(1,num +1):
        if num % i == 0:
            count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")