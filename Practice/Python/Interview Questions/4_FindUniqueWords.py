# Find Unique Words

arr = ["Hello, how are you?", "I am fine, thank you!", "How about you?",
       "I am doing well, thank you!",
       "What are you doing?", "I am working on a project.", "That sounds interesting!"
      ]

unique_words = []

pun = ",?!."

for sentence in arr:
    sentence = sentence.lower()
    for p in pun:
        sentence = sentence.replace(p, "")
    words = sentence.split()
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

print("Unique words are:")
for word in unique_words:
    print(word)