s = input("Enter Your String: ").strip()
count = 1

for ch in s:
    if ch == " ":
        count += 1

print(count)
