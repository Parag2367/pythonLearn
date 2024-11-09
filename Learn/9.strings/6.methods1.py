# methods part 1

# a = "parag is learning python coding 12345&&&"

# the methods gives the output

# b = a.title()
# print(b)

# c = a.capitalize()
# print(c)

# d = a.upper()
# print(d)

# e = a.lower()
# print(e)

# f = a.swapcase()
# print(f)


# all these methods gives output as boolean

st = "Parag learn"
st1 = "parag123"
st2 = "A  B  C DFRTH 0987654$$$"

a = (
    st.islower()
)  # checks if all are lower case, they wiil only check for alphabet in the string , they wont care for other
print(a)

a = (
    st2.isupper()
)  # checks if all are upper case, they wiil only check for alphabet in the string , they wont care for other
print(a)

a = st.isalpha()  # checks if all are alphabets only it should not have even any spaces
print(a)

a = st.isdigit()  # checks if all are digits
print(a)

a = (
    st1.isalnum()
)  # # checks if all are combination of alphabets or numbers only no space and special characters
print(a)

a = st.isspace()  # checks if all are spaces, \n, \t
print(a)


z = "parag123"

if z.isdigit():
    z = int(z)
    print(z, type(z))
else:
    print("it is not a digit")
