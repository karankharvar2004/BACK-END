s = input("Enter Your String: ").lower()
vowels = "aeiou"
v = c = 0

for i in s:
    if i >= 'a' and i <= 'z':
        if i in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)