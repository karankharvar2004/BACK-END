from collections import Counter

sentences = [
    "Python is amazing! Do you like Python?",
    "I love coding in Python.",
    "Python, Java, and C++ are popular programming languages.",
    "Learning Python is fun.",
    "Python is used for data analysis, machine learning, and web development."
]

# punctuation to remove
punctuation = ".,!?;:"

all_words = []
python_sentence_count = 0

for sentence in sentences:
    # check if sentence contains 'python'
    if "python" in sentence.lower():
        python_sentence_count += 1

    # convert to lowercase
    sentence = sentence.lower()

    # remove punctuation
    for p in punctuation:
        sentence = sentence.replace(p, "")

    # split into words
    words = sentence.split() 

    # add words to main list
    all_words.extend(words)

# count word frequency
word_count = Counter(all_words)

# top 5 most common words
top_5 = word_count.most_common(5)

# unique words count
unique_words = len(word_count)

# output
print("Top 5 words:", top_5)
print("Unique words count:", unique_words)
print("Sentences containing 'python':", python_sentence_count)
