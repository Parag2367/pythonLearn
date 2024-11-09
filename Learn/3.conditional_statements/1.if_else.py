# if, elif,else

# age = int(input("Enter Age = "))

# if age > 18:
#     print("You can vote !")

# else:
#     print("You cannot vote as your age is", age)

# print("ok done! Bye")

#############

num1: int = int(input("Enter number = "))
num2: int = int(input("Enter number = "))

if num1 > num2:
    print(f"{num1 = } is greater")

elif num1 == num2:
    print(" Both are equal")

else:
    print(f"{num2 = } is greater")
