# result always in boolean (True False)
a = 30
b = 10

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)


print(int(a > b))  # True ke liye 1
print(int(b > a))  # False ke loiye 0


"""
Note:
Arithmetic operators take precedence over logical operators. 
Python will always evaluate the arithmetic operators first (** is highest, then multiplication/division, then addition/subtraction). 
Next comes the relational operators.


Relational:
First, less than ( < ), 
less than or equal to ( <= ), greater than ( > ), and greater than or equal to ( >= ). Then, equal to ( = ) and not equal to ( != ).

Arithmetic:
** then BODMAS

Logical:
Logical operators have operator precedence the same as other operators (relational, arithmetic, etc.).
The highest precedence belongs to not , followed by and , and finally by or 

"""
