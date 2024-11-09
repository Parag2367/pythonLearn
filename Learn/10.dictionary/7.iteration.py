my_dict = {
    "name": "Parag",
    "surname": "Patondikar",
    "Age": 29,
    "Profession": "Software Engineer",
}

print(list(my_dict))  # creates a list of keys
print(tuple(my_dict))  # creates a tuple of keys

print(my_dict.keys())

for k in my_dict.keys():
    print(k)

for k in my_dict.keys():
    print(k, my_dict[k])

for k in my_dict.keys():  # this will give values
    print(my_dict[k])

for v in my_dict.values():  # this will give values
    print(k)


for k, v in my_dict.items():
    print(k, v)


my_dict["Age"] = 30
print(my_dict)


my_dict = {"name": "Parag", "age": 23, "gender": "Male"}

"""
name -> Parag,
age -> 23,
gender -> Male
"""

# tuple unpacking, as the method items will take k,v as tuples

print(my_dict.items())
print(type(my_dict.items()))

for k, v in my_dict.items():
    print(f"{k} -> {v}")
