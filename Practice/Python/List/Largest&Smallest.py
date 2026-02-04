# arr = list(map(int, input("Enter Your Values: ").split()))

arr = [48, 56, 100, 99, 27, 27]

largest_num = smallest_num = arr[0]

for i in arr:
    if i > largest_num:
        largest_num = i
    if i < smallest_num:
        smallest_num = i
    
print("Largest Number:",largest_num)
print("Smallest Number:",smallest_num)