# Find first repeating element

arr = [10, 20, 30, 40, 30, 20, 50]

new_arr = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print("First repeating element:", arr[i])
            break
    else:
        continue
    break