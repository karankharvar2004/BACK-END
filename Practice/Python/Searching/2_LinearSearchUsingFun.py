# Linear Search by defining Function

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 20, 30, 40, 50]
result = linear_search(arr, 40)

if result != -1:
    print("Found at index:", result)
else:
    print("Not found")
