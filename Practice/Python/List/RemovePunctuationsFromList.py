str_list = ["Hello!!! How are you??"]

punctuations = "!?"

string = str_list[0].lower()

for p in punctuations:
    string = string.replace(p, "")

words = string.split()

longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word

print("Longest Word: ",longest_word)
print("Shortest Word: ",shortest_word)