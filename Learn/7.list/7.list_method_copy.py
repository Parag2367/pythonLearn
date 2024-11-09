my_list = [23, 34, 56, 76, 56.655, [23, 34, 45], True, "Parag"]

# copy method very important: suppose we have to copy a list

b = my_list  # this will make both b and my_list to point at same address for the variable(list),
# as we know in programming variable does not store value they store address of that value
# so b = my_list will point to same adress see below,
# and suppose if we change anything in my_list , same changes will happen on b as well
# so if you want to copy use copy as it will create a different id , so it will not affect the original list

# my_list[2] = 0
# print(my_list)
# print(id(my_list))

# print(b)
# print(id(b))

"""
shallow copy
"""
# so to avoid this issue always use copy , as copy will store the new variable at a new address
# c will be a new list

c = my_list.copy()  #

my_list[2] = 0
print(f"{my_list =}")
print(f"{id(my_list) = }")
print(f"{id(my_list[1]) = }")
print("-----Shallow copy--------------")
print(f"{c = }")
print(f"{id(c) = }")
print(f"{id(c[1]) = }")
print("--------------------------------")
"""
output: shallow copy example, this internal elements will still have same id but in deep copy everything changes

my_list =[23, 34, 0, 76, 56.655, True, 'Parag']
id(my_list) = 2485168789056
id(my_list[1]) = 140736602761032
c = [23, 34, 56, 76, 56.655, True, 'Parag']
id(c) = 2485170174912
id(c[1]) = 140736602761032
"""


"""
Works only: [23,34,56,[34,45,33,40],56,55] if there is a iterable item inside a list, not for simple list
Deep copy : it will only work if there is another iterable element inside list, llike list in list
"""
import copy
from copy import deepcopy

my_list[2] = 1000
print(f"{my_list =}")
print(f"{id(my_list) = }")
print(f"{id(my_list[5][0]) = }")

print("----------Deep Copy-----------------")

d = copy.deepcopy(my_list)
e = deepcopy(my_list)
d[5][0] = 100
print(f"{my_list =}")
print(f"{d =}")
print(f"{id(d) = }")
print(f"{id(d[5][0]) = }")
