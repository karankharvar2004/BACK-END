# Find first non-repeating element

arr = [10, 20, 30, 40, 30, 20, 50]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

for i in arr:
    if freq[i] == 1:
        print("First non-repeating element:", i)
        break