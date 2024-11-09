"""
revealing error name and type 
we have used:
Exception as e (we can give any name)
type(e).__name__
"""

# try:
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a number = "))
#     print(a / b)
# except Exception as e:
#     print(e)
#     # print("Some error occured")
#     # print(type(e))
#     print(type(e).__name__)

#     print(f"{type(e).__name__} message: {e}")

# another
try:
    mylist = [22, 33, 44, 55, "parag"]
    index = int(input("Enter an index = "))
    print(mylist[index])
except Exception as e:
    print("some error occured")
    print(f"{type(e).__name__} : {e}")
