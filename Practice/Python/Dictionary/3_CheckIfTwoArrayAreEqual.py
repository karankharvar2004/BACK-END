# Check if two arrays are equal

arr1 = [10, 20, 30, 40, 50]
arr2 = [10, 20, 30, 40, 50]

if len(arr1) != len(arr2):
    print("Not Equal")

# Case 1: Same Elements + Same Order
print(arr1 == arr2)

# Case 2: Same Elements, Order Doesn’t Matter
if sorted(arr1) == sorted(arr2):
    print("Matched")
else:
    print("Not Matched")