"""
write mode : it will create file if it is not available no error
if we write something to a file it will overwrite whole file with new content by default
"""

with open("abc.txt", "w") as file:
    file.write("parag")
    file.write("name")  # it will add just next to g

with open("abc.txt", "w") as f:
    f.write("quick")


with open("abc.txt", "a") as fo:
    fo.write("there")  # it will add just next to last character of data in file
