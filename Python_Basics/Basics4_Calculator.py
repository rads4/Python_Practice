first = input("Enter first number:")
operator = input("Enter operator: [+, -, *, /, %]:")
second = input("Enter second number:")

if(operator=="+"):
    print("The sum of first and second number is:", int(first) + int(second))
elif(operator=="-"):
    print("The difference of first and second number is:", int(first) - int(second))
elif(operator=="*"):
    print("The product of first and second number is:", int(first) * int(second))
elif(operator=="/"):
    print("The division of first and second number is:", int(first) / int(second))
elif(operator=="%"):
    print("The remainder of first number divided by the second number is:", int(first) % int(second))
else:
    print("Invalid operator") 