# Exercise: Check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for item in some_list:
    if some_list.count(item) == 2 and duplicates.count(item) == 0:
        duplicates.append(item)

print(duplicates)
