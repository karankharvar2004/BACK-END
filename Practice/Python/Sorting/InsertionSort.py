# Insertion Sort: It is a simple sorting algorithm that builds the sorted list one item at a time. 
# It repeatedly takes the next unsorted element and inserts it into the correct position in the sorted 
# part of the list until the entire list is sorted.

arr = [5, 3, 8, 4]

n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    arr[j + 1] = key

print(arr)
