my_dict = {
    "name": "Parag",
    "surname": "Patondikar",
    "Age": 29,
    "Profession": "Software Engineer",
    "Physics": 45,
    "Maths": 55,
    "Chemistry": 60,
}


# getting to the element in dictionary if key does not exist it will give error
print(my_dict["name"])
print(my_dict["Age"])

# another way , if key does not exist it will give None, so we can use it
r = my_dict.get("name")
print(r)

t = my_dict.get(
    "maths", 0
)  # it will give the original value of key, if value is not there it will assign 0
print(t)

y = my_dict.get("marks", 0)  # it will create a new key:value pair
print(y)


############
k = input("Enter a key = ")
result = my_dict.get(k)

if result is not None:
    print(result)

else:
    print("Not a key")


###########

total = print(my_dict["Physics"] + my_dict["Maths"] + my_dict["Chemistry"])
