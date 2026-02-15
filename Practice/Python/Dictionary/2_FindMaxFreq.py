# Find element with max frequency

arr = [10, 20, 30, 40, 20, 60, 50, 20]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

max_count = 0
max_element = None

for key, value in freq.items():
    if value > max_count:
        max_count = value
        max_element = key

print("Element with maximum frequency:", max_element)
print("Frequency:", max_count)

# min_count = float('inf')
# min_element = None

# for key, value in freq.items():
#     if value < min_count:
#         min_count = value
#         min_element = key
    
# print("Element with minimum frequency:", min_element)
# print("Frequency:", min_count)