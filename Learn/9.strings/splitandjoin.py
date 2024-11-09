""" 
split method , it will always give list
"""

# my_list = "Hello welcome to the world of python"

# words = (
#     my_list.split()  # this will give list always
# )  # we can use split for any character eg split("-"), split(","), by default it takes spaces
# print(words)

# for a in words:
#     print(a)

# rever = words[::-1]
# print(rever)

mystr = "python is a gooood language"

words = mystr.split("o")
print(words)

# output:
# ["pyth", "n is a g", "", "d language"] #if simulataneous split character are there it will create a blank
# ['pyth', 'n is a g', '', '', '', 'd language']

"""Join method : syntax (''.join(<name>))"""

# my_list = ["hello", "welcome", "to", "the", "world", "of", "python", 768]

# # joined = " | ".join(my_list) # this will give a string
# # print(joined)

# # suppose if we pass any integer or other datatype inside list .join(<list_name>) will throw error
# # TypeError: sequence item 7: expected str instance, int found
# # so to avoid it we will use list comprehension and convert it to str

# joined_all = "|".join(str(i)[::-1] for i in my_list)
# print(joined_all)
