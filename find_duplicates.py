# Exercise: Check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for item in some_list:
    if some_list.count(item) == 2:
        duplicates.append(item)

print(list(set(duplicates)))
