def make_pretty(func):
    def inner():
        print("I am decorated")
        func()

    return inner


def make_prettier(func):
    def inner():
        print("I am more decorated ")
        func()

    return inner


@make_prettier
@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()


# def decorators(func):
#     def inner():
#         print("")
#         func()

#     return inner


# @decorators
# def ord():
#     print("yes")


# ord()
