# Count even and odd numbers

arr = [25, 45, 66, 82, 69, 32, 44]

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even += [i]
    else:
        odd += [i]

print("Even Numbers are:",even)
print("odd Numbers are:",odd)