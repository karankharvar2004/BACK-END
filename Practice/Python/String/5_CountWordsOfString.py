# Count words in a string

str = input("Enter Your String: ")

count = 0

words = str.split()

for word in words:
    count += 1
 
print(count)