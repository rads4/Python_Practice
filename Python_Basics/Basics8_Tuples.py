# Tuples are immutable - cannot be changed once created
# Tuples use parentheses ()

marks = (95, 98, 92, 97, 97, 97)
# marks{0} = 99  # This will raise an error

print(marks.count(97))  # count of 97
print(marks.index(98))  # index of 98

# Not necessary to use parentheses
marks = 95, 98, 92, 97
print(marks)
