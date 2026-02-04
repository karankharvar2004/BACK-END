Sentences = [
            "Hello!! My Favorite Programming Language is Python!!",
            "It is a General Purpose Programming language.",
            "Python is based on Object Oriented Programming Concept."]

punctuations = "!."

count = 1

for sentence in Sentences:
    sentence = sentence.lower()

    for p in punctuations:
        sentence = sentence.replace(p, "")

    words = sentence.split()
    print("Sentence", count, "→", len(words), "words")

    count += 1
