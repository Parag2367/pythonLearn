# importing the module
import csv

# open the file in read mode
filename = open("data.csv", "r")

# creating dictreader object
file = csv.DictReader(filename)

# creating empty lists
name = []

# iterating over each row and append
# values to empty list
for col in file:
    name.append(col["name_azure"])


print(name)
