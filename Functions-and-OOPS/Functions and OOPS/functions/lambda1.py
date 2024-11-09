# Take a argument which will be number
# Make a list 0 to N

make_list = lambda n: [i for i in range(0, n + 1)]

length = int(input("Enter length = "))
list1 = make_list(length)
list2 = make_list(15)

print(list1)
print(list2)
