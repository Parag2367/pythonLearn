# dictionary in dictionary

students = {
    "Parag": {"roll": 34, "age": 20, "maths": 45, "phy": 50},
    "Rahul": {"roll": 44, "age": 22, "maths": 49, "phy": 44},
    "Ravi": {"roll": 22, "age": 21, "maths": 39, "phy": 40},
}


# print(students["Parag"])
# print(type(students["Parag"]))

# print(students["Parag"]["roll"])
# print(students["Parag"]["age"])


# for name, details in students.items():
#     age = details["age"]
#     total = details["maths"] + details["phy"]
#     print(f"{name} age = {age} -> {total}")


"""
name has score total marks
"""

# for name, details in students.items():
#     total = details["maths"] + details["phy"]
#     print(f"{name} has scored {total}")

# another method

# for name, details in students.items():
#     total = details.get("maths", 0) + details.get("phy", 0)
#     print(f"{name} has scored {total}")

"""
add total in inside dict
"""
# for name, details in students.items():
#     total = details.get("maths", 0) + details.get("phy", 0)
#     details["total"] = total
# print(students)


"""
sorted
"""

print(students)

sorted_maths = sorted(students.items(), key=lambda x: x[1]["maths"])
sorted_maths_r = sorted(students.items(), key=lambda x: x[1]["maths"], reverse=True)

print(sorted_maths)
print(sorted_maths_r)
