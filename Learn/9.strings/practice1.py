"""
Write a program to reverse the order of words.
"""

# my_words = input("Enter a sentence = ")

# words = my_words.split()
# words = words[::-1]  # we can do overwrite

# joined = " ".join(words)
# print(joined)


"""
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.
"""

# my_string = input("Enter a string = ")
# words = my_string.split()

# result = " ".join(i.capitalize() for i in words)
# print(result)


"""
Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you"
"""

my_string = input("Enter a string = ")
result = ""

for a in my_string:
    if a == a.upper():
        a = "_" + a.lower()
        result = result + a

    else:
        result = result + a
print(result)


## by list compreshnsion:

my_string = input("Enter a string = ")
result = "".join()


###########
my_string = "aaabbcc"
