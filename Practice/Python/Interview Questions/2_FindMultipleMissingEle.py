# Find Multiple Missing Elements

arr = [1, 2, 4, 5, 7]

n = 7  #last number of sequence (1 to 7)

for num in range(1, n+1):
    found = False

    for i in range(len(arr)):
        if arr[i] == num:
            found = True
            break

    if not found:
        print("Missing Number is: ",num)