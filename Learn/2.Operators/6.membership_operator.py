# IN , NOT IN  Operators

my_list = [23, 34, 56, 76, "Parag", 56.655, True, 56]
# in , not in  are the operators
print(23 in my_list)

num = int(input("Enter the number = "))

if num in my_list:
    print("Yes")
else:
    print("No")


## alternative way , not popular:

num = int(input("Enter the number = "))

if my_list.count(num) > 0:
    print("Yes")
else:
    print("No")
