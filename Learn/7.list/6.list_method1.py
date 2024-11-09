my_list = [23, 34, 56, 76, "Parag", 56.655, True, 56]
my_list1 = [23, 34, 56, 76, 56.655, 56]

# pos = my_list.index(56)  # it will give the index of first of same element
# print(pos)

"""
sort method
"""
# my_list1.sort()
# print(my_list1)

# my_list1.sort(reverse=True)
# print(my_list1)

# my_list1.reverse()
# print(my_list1)

"""
Difference between append and extend
"""
my_list1.append(["parag", "Ram", True])
print(my_list1)

# my_list1.extend(
#     ["parag", "Ram", True]
# )  # this will append the elements of collection rathen than collection , it will need collection which are iterable
# print(my_list1)

"""
Count method
"""
# cnt = my_list.count(
#     56
# )  # it will count the no.of times the element is present in the list, it will give the output
# print(cnt)

"""
clear method
"""
# my_list1.clear()  # id will be same
# print(my_list1)

# my_list = []
# print(id(my_list)) # id will be different
