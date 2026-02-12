# Count Frequency of Each Character

str = input("Enter Your String: ").lower()

freq = {}


# Count Frequency for each "character" in String

for i in str:
    if i != "":
        freq[i] = freq.get(i, 0) + 1

print(freq)




# Count Frequency for each "word" in String

# words = str.split()

# for i in words:
#     if i != "":
#         freq[i] = freq.get(i, 0) + 1

# print(freq)
