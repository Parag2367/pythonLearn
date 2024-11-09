# args and kwargs


# args always gives output as a tuple of arguments
def add(name, *args):
    print(name)
    print(args)


add("Parag", 10, 20, 30, 20)


def add1(name, *x):  # we can give any name to variable not neccesary args
    print(name)
    print(x)


add("Parag", 10, 20, 30, 20, True)


def add2(name, *args):
    print(name)
    print(args)


# add2(name='Parag',10,20,30)  # we cannot use the named parameter when we are using args


## kwargs (it always take key=value pair)
# it will always give dictionary as output
# note: named arguments are always passed at the end that is a rule in python


def ad(*args, **kwargs):
    print(args)
    print(kwargs)


ad(10, 20, 30, 40, name="Parag", age=23)
ad(name="parag", age=30)


# def ad2(**kwargs,*args) # not allowed
# # note: named arguments are always passed at the end


def ad3(address, phone, *args, name="", age=0, **kwargs):
    print(address)
    print(phone)
    print(args)
    print(kwargs)


# practice
def calculate_total_cost(*args, **kwargs):
    discount = kwargs["discount"]
    if len(args) == 0 or discount < 0 or discount > 100:
        print("invalid or wrong discount")
        return
    total_bill = sum(args)
    discount_amt = total_bill * (discount / 100)
