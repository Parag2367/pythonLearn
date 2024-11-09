"""
reading binary files
"""

with open("filname.pdf", "rb") as file:
    data = file.read()
    print(data)
