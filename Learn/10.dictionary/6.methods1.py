mydict = {
    "pysics": 54,
    "maths": 70,
    "english": 60,
    "hindi": 65,
    "sanskrit": 65,
    "pe": 0,
}

# clear method : it will clear the dictionary
# mydict.clear()
# print(mydict)


# from keys method:
# a = ["name", "age", "gender"]
# b = ["parag", 27, "Male"]

# mydict = {}
# for i in range(len(a)):
#     mydict[a[i]] = b[i]

# print(mydict)

# # we can also use fromKeys method

# mydict1 = dict.fromkeys(a, 0)  # first arg is a iterable, second arg is a value
# print(mydict1)


# best way
user_key = input("Enter a key = ")

if user_key in mydict:
    print(mydict.get(user_key))
else:
    print("Not a key")

# another way
result = mydict.get(user_key)
if result:
    print(result)
else:
    print("No key found error!")


# another way
result = mydict.get(user_key, None)
print(result)
