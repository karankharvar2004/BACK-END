# Merge two lists

arr1 = [10, 20, 30, 40]
arr2 = [40, 50, 60, 70]

new_arr = []

arr1.extend(arr2)

for i in arr1:
    if i not in new_arr:
        new_arr += [i]

print(new_arr)



# for Time Complexity

# new_arr = list(dict.fromkeys(arr1 + arr2))
# print(new_arr)
