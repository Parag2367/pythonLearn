# students = {
#     "Parag": {"roll": 34, "age": 20, "marks": [34, 45, 56, 78]},
#     "Rahul": {"roll": 44, "age": 22, "marks": [45, 54, 55, 70]},
#     "Ravi": {"roll": 22, "age": 21, "marks": [44, 43, 40, 44]},
# }

# for name, details in students.items():
#     total = 0
#     for a in details["marks"]:
#         total = total + a
#     print(f"{name},total = {total}")


######################
# dictionary in dictionary in dictionary

students_details = {
    "Parag": {"roll": 34, "age": 20, "marks": {"phy": 45, "chem": 40, "maths": 55}},
    "Rahul": {"roll": 44, "age": 22, "marks": {"phy": 33, "chem": 50, "maths": 65}},
    "Ravi": {"roll": 22, "age": 21, "marks": {"phy": 25, "chem": 30, "maths": 45}},
}

for a in students_details.keys():
    print(students_details[a]["marks"])
