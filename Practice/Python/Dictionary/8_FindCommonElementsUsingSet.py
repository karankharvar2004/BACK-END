# Find common elements using set

arr1 = [10, 20, 30, 40, 50]
arr2 = [30, 40, 60, 70]

common = list(set(arr1) & set(arr2))

print(common)


# set2 = set(arr2)

# common = []

# for num in arr1:
#     if num in set2:
#         common.append(num)

# print(common)