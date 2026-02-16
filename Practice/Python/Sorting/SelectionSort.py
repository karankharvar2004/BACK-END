# Selection Sort: It is a simple sorting algorithm that divides the input list into two parts: 
# the sorted part and the unsorted part. 
# It repeatedly selects the smallest (or largest) element from the unsorted part and moves 
# it to the end of the sorted part until the entire list is sorted.

arr = [5, 3, 8, 4]

n = len(arr)

for i in range(n):
    min_index = i
    
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
            
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
