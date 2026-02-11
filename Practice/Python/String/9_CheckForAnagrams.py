# Check if two strings are anagrams

str1 = input("Enter Your 1st String: ")
str2 = input("Enter Your 2nd String: ")

if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Not Anagrams")
