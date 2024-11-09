"""
opening using 'with' , we donot have to use close in this case
"""

with open("hello.txt", "r") as file:
    data = file.read()
    print(data)
