"""ASCII codes"""

# Decimal, Hexadecimal,Octadecimal
# ord()

# first_ch = "a"
# second_char = "A"

# print(first_ch > second_char)  # True , because ascii code of a is greater then A

# # how to print ascii code
# ch = "c"
# print(ord(ch))
# num = 99
# print(chr(num))


# mys = "python is a very good language"

# cont = 0
# for ch in mys:
#     if ch == "a" or ch == "A":
#         cont = cont + 1
# print(cont)


# another way is using ascii value

mys = "python is a very good language"

cont = 0
for ch in mys:
    if ord(ch) == 100:
        cont = cont + 1
print(cont)
