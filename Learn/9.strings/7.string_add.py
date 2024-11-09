"""
Keep adding string untill user types quit
"""

# my_string = ""

# while True:
#     char = input("Enter a character = ")
#     if char == "quit":
#         break
#     my_string += char

# print(my_string)


"""
swap case , exclude special symbol
"""

my_string = "pyTHon is GOOd@@#$"

# result = ""
# for a in my_string:
#     if a.isalpha():
#         if a.islower():
#             result += a.upper()
#         else:
#             result += a.lower()
#     else:
#         result += a

# print(result)


# another approach
result = ""
for a in my_string:
    ascii_code = ord(a)
    if ascii_code >= 97 and ascii_code <= 122:
        capital_letter = chr(ascii_code - 32)
        result += capital_letter
    elif ascii_code >= 65 and ascii_code <= 90:
        small_letter = chr(ascii_code + 32)
        result += small_letter
    else:
        result += a

print(result)
