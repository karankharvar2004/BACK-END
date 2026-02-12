# Check Substring

str = input("Enter Your String: ")
sub_str = input("Enter Your SubString: ")

str = str.lower()
words = str.split()

if sub_str in words:
    print(sub_str,"is present in String")
else:
    print(sub_str,"is not present in String")