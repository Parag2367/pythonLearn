# input : by default it stores string always
# so to change the input to desired data type we can use type casting

x = input("what do you think! ")
print("you eneterd", x)

name = input("What is your name = ")
gender = input("What is your gender = ")
age = int(input("What's your age = "))

print(f"my name is {name}")
print(f"my gender is {gender}")
print(f"my age is {age}")

print(f"{name = }")
print(f"{age = }")
print(f"{gender = }")
