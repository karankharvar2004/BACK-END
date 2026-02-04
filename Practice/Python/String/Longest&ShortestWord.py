string = "Hello, My Favorite programming Language is Python!!"

words = string.split()

largest_word = words[0]
shortest_word = words[0]


for word in words:
    if len(word) > len(largest_word):
        largest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word
    
print("Largest Word: ",largest_word)
print("Shortest Word: ",shortest_word)