"""
dict
"""

mydict = {"name": "parag", "age": 18, "gender": "Male", "education": "Graduate"}

try:
    key = input("Enter a key = ")
    print(f"{key} : {mydict[key]}")
except KeyError:
    print(f"{key} not found error")
except:
    print("Some other error happend")
