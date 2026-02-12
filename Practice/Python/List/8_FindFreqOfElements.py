# Find frequency of elements

arr = [10, 20, 20, 30, 40, 40, 50]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1
    
print(freq)