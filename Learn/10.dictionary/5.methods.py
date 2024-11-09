my_dict = {
    "name": "Parag",
    "surname": "Patondikar",
    "Age": 29,
    "Profession": "Software Engineer",
}

# add/update method1:
# the key and value will be added if that key is not there , but it will update if key is there

# method1
my_dict["Age"] = 34
print(my_dict)

# it will update the value of key, but if it is not available it will add the new key value
my_dict["xyz"] = 76
print(my_dict)

# method2 multiple updation is possible at once by this
my_dict.update({"marks": 99, "address": "Pune"})
print(my_dict)


# Remove method:

del my_dict["marks"]
print(my_dict)

del my_dict["xyz"]

del my_dict["number"]  # it will delete only if that key is there

# del my_dict  # it will remove the whole dict, no variable found
my_dict.pop("Age")
print(my_dict)


# it needs atleat one argument in case of dictionary , but in case of list it will pop last element
# my_dict.pop()
# print(my_dict)

my_dict.popitem()  # it will pop the last item, it does not take any argument
print(my_dict)
