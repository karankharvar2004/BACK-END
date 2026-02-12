# Remove duplicates from list

arr = [10, 20, 20, 30, 40, 40, 50]

new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)
        # new_arr += i
        
print(new_arr)