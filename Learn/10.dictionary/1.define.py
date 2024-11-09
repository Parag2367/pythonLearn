"""
Dictionary: keys are case sensitive
"""

my_dict = {
    "name": "Parag",
    "surname": "Patondikar",
    "Age": 29,
    "Profession": "Software Engineer",
    1: 34,
    2: 34,
    True: 23,
    False: 23,
}

print(my_dict)

# key is always unique, suppose if key is repeated ,
# so the latest value will be overwritten, always one key will be printed with latest value of it, it will not give any error
print(my_dict.keys())

# this is not aloowed rather we can use my_dict.items(), my_dict.values(), my_dict.keys()
# for a in my_dict():
#     print(a)

for a in my_dict.items():
    print(a)
