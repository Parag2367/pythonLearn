# giving a default value of one parameter, we can pass it in argument that will overwrite this default value
def add(num1, num4, num2=0, num3=0):
    total = num1 + num2
    print(total)


add(50, 43)  # no error as num3 and num4 are having a default parameter
# default parameter to be on right and required on left always
