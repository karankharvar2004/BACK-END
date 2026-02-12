# Find largest and smallest element

arr = [50, 40, 70, 60, 20]

largest_num = arr[0]
smallest_num = arr[0]

for i in arr:
    if i > largest_num:
        largest_num = i
    if i < smallest_num:
        smallest_num = i

print(largest_num,"is a Largest Number")
print(smallest_num,"is a Smallest Number")