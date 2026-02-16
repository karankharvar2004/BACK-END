# Word frequency in a sentence

arr = "python is easy, and python is powerful!"

pun = ",!"

arr = arr.lower()

for p in pun:
    arr = arr.replace(p,"")

words = arr.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
