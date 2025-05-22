students = ["Steve", "Natasha", "Tony", "Bruce", "Clint"]

# Break Keyword
# print all names but stop when Bruce is reached
# for i in students:
#     if i == "Bruce":
#         break
#     print(i)


# Continue Keyword
# print all names but skip Tony
for i in students:
    if i == "Tony":
        continue
    print(i)

