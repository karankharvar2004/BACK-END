list = [11, 12, 12, 13, 14, 14, 15, 16, 16]
unique_list = []

for i in list:
    if i not in unique_list:
        unique_list.append(i)

print("Original list:", list)
print("List after removing duplicates:", unique_list)