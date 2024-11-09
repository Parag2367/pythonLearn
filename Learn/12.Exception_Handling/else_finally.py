"""
if age < 18 raise error
"""

try:
    age = int(input("Enter age of voter = "))
    if age < 18:
        raise ZeroDivisionError  # we are raising any random error not realted
    print("You can vote")
except ZeroDivisionError:  # referencing line 8
    print("You can not vote")
except ValueError:
    print("Enter proper age value")
except:
    print("Some other error occured")
else:  # this will run only if try block is successful
    print("everything works fine")
finally:  # this will run always inspite of anything
    print("This is finally")
