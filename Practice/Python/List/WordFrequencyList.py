list = ["I love Python and I love coding"]

str = list[0].lower()
words = str.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)