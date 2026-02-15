# Check if array is sorted

arr = [20, 40, 60, 30, 10, 50]

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        print("Not Sorted")
        break
else:
    print("Sorted") 
