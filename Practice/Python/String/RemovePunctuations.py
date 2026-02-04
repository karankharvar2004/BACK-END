string = "Hello!!! How are you??"
# output: "Hello How are you"

punctuations = "!?"

for p in punctuations:
    string = string.replace(p, "") 

print(string)       