age_str = input("Enter your age:")
age = int(age_str)  # Convert the input string to an integer
if age >= 18:
    print("You are an adult, you can vote")

elif (
    age < 18 and age > 3
):  # if first condition is false, it will check the next condition
    print("You are in school")
else:
    print("You are a child")
