# Find Longest Word in a String

str = input("Enter Your String: ")

longest_Str = ""

words = str.split()

for word in words:
    if len(word) > len(longest_Str):
        longest_Str = word

print(longest_Str,"is a Longest Word!!")