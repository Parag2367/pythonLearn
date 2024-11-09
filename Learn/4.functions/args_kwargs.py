# *args : gives tuple
# **kwargs: gives dictionary


# def example(*args):
#     print(f"{args}")
#     print(sum(args))


# example(34, 45, 66, 77)


# ################
# def example1(**kwargs):
#     print(f"{kwargs}")


# # example1(
# #     45, 56, 78
# # )  # we cannot pass this to kwargs, they only take keyword argumnet(name = <>,age=<>)

# example1(name="Parag", age=18, gender="male")


def run(n1, n2, n3, *args, **kwargs):
    print(f"{n1 = }")
    print(f"{n2 = }")
    print(f"{n3 = }")
    print(f"{args = }")
    print(f"{kwargs = }")
    for k, v in kwargs.items():
        print(k)
        print(v)


run(2, 3, 4, 45, 667, 778, 88, name="Parag", age=16)
