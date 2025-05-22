# Inbuilt functions:
# int()
# str()
# bool()
# float()
# list()
# tuple()
# dict()
# len()
# max()
# min()
# sum()

# Module Functions - related variables/functions stored in one file
# import math
# print(dir(math))  #lists out all math functions

# importing specific functions:
# from math import sqrt
# print(sqrt(4))


# importing all functions:
# from math import sqrt
# print(sqrt(4))


# User-defined functions:
# def function_name(parameters):
#     # function body
#     return value


def add(a, b):
    print(a + b)


add(2, 4)  # caling the function - executing


# using a by default parameter
def add(a, b=4):
    print(a + b)


add(2)