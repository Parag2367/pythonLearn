"""
index error
"""

# try:
#     mylist = [22, 34, 56, 78]
#     index = int(input("Enter an index value = "))
#     print(mylist[index])  # chances of out of index error
# except:
#     print("Some error occured")


""" 
another example : to handle the inbuilt error just use there name and we can print our own message
 as an error have name: message
"""

try:
    mylist = [22, 34, 56, 78]
    index = int(input("Enter an index value = "))
    print(mylist[index])
    print(5 / 0)
except IndexError:
    print(f"{index} is out of index")
except ZeroDivisionError:
    print("cannot be divided by zero")
except:
    print("some error occured")
