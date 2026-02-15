# Count frequency using dictionary

arr = [20, 50, 40, 20, 40, 50, 60, 70]

freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)