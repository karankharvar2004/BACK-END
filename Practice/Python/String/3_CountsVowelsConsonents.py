# Count vowels and consonants

str = input("Enter Your String: ").lower()

vowels = "aeiou"

vols = 0
cons = 0

for i in str:
    if i.isalpha():
        if i in vowels:
            vols += 1
        else:
            cons += 1

print("Vowels  =",vols)
print("Consonants =",cons)