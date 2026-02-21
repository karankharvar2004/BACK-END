arr = ["Hello!!! How are you??"]

pun = "!?"

arr = arr[0].lower()

clean_words = []

words = arr.split()

for word in words:
    for p in pun:
        word = word.replace(p, "")
    clean_words.append(word)

print(clean_words)
