str = "I love Python and I love coding"
# output: {'i': 2, 'love': 2, 'python': 1, 'and': 1, 'coding': 1}


str = str.lower()
words = str.split()

freq = {}


for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
