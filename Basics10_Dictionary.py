# dictionary uses key-value pairs
# dictionary is unordered
# dictionary is mutable
# dictionary uses curly braces
# dictionary allows duplicates
# dictionary is indexed

marks = {"English": 95, "Maths": 92, "Science": 99}
print(marks)

print(marks["Maths"])  # access value using key
print(marks.get("English"))  # access value using get method

# adding new elements
marks["Physics"] = 97
print(marks)

# updating existing elements
marks["Maths"] = 99
print(marks)
