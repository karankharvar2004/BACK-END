# Sort Dictionary By Values: This is a simple sorting algorithm that sorts a dictionary based on its values. 
# It can be implemented using the built-in sorted() function with a custom sorting key.

d = {"apple": 3, "banana": 1, "cherry": 2}

sorted_items = sorted(d.items(), key=lambda x: x[1])

sorted_dict = dict(sorted_items)

print(sorted_dict)
