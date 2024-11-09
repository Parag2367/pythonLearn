"""
multiple user input
"""

# def writing(userinput, filename):
#     with open(filename + ".txt", "w") as file:
#         file.write(userinput)


# filename = input("Enter filename without extension = ")

# userinput = ""
# while True:
#     u_inp = input("Enter you data = ")
#     if u_inp.lower() == "q":
#         break
#     userinput = userinput + u_inp
#     userinput = userinput + "\n"  # doing this to change to anew line


# writing(userinput, filename)
# writing(
#     userinput[:-1], filename
# )  # added [:-1] so that it doesnot go to end that is it should not add last \n


#######################

# another way


def create(filename):
    with open(filename, "w") as file:
        while True:
            u_inp = input("Enter your data = ")
            if u_inp.lower() == "q":
                break
            file.write(u_inp + "\n")


create("testing")
