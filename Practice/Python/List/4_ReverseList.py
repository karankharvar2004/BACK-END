# Reverse a list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev = []

for i in arr:
    rev = [i] + rev

print(rev)
