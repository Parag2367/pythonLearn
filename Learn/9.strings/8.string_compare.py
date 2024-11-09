"""
String comaprison happens on basis of ascii code
"""

my_string1 = "PYThon"
my_string2 = "python"


print(my_string1 > my_string2)


char = "p"

if "a" <= char <= "z":
    print(f"{char} is small letter")
else:
    print("It is a capital letter")
