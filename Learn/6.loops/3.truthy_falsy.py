"""
truthy
falsy

value:

int: anything except 0 == truthy
int : 0 == falsy

float: anything except 0 == truthy
float : 0 == falsy

string: anything except "" == truthy
string : "" == falsy

boolean: true == truthy
boolean : false == falsy

None: falsy always
"""

# name = input("Enter your name = ")

# if name:
#     print(name)

# else:
#     print("no name")


a = None
if a:
    print("Hello")
else:
    print("it is none")
