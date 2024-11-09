"""
Keys: all object except mutable object(List) can be key
"""

dictionary = {
    "name": "Parag",
    "age": 28,
    "gender": "Male",
    "marks": [2, 3, 4, 5],
    "marks1": (2, 3, 4, 5),
    1: "abc",
    2: 23,
    3: 3,
    True: 34,
    False: False,
    0: True,  # this will overwrite False key
    (1, 2, 3): "Ravii",
    None: "every",
}

print(dictionary)
