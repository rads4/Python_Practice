# SETS stores only unique values
# SETS is unordered - no fixed sequence
# SETS is mutable
# SETS uses curly braces

marks = {95, 98, 92, 97}

# does not allow duplicates
# marks = {97, 98, 92, 97, 97}
# print(marks)

# index does not exist here
# print(marks[0]) # This will raise an error

# using loop to iterate
for i in marks:
    print(i)
