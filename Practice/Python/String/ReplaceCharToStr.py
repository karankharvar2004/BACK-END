s = input("Enter Your String: ")
old = input("Old char: ")
new = input("New char: ")

result = ""

for ch in s:
    if ch == old:
        result += new
    else:
        result += ch

print(result)
