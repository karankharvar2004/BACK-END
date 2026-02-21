# Find Missing Elements

arr = [1, 2, 4, 5, 7]

n = len(arr) + 1
total_sum = n*(n+1)//2
array_sum = sum(arr)

missing_number = total_sum - array_sum

print("Missing Number is:",missing_number)