"""
Lambda function they are anonymous functions, they are written in a single line
"""

# normal function
# def add(n1, n2, n3):
#     total = n1 + n2 + n3
#     return total


# a = add(23, 32, 43)
# print(a)

# Lambda function
# lambda parameters : return
# b = lambda n1, n2, n3: n1 + n2 + n3
# print(b(23, 32, 34))


# # make a list of numbers
# make_list = lambda n: [i for i in range(0, n + 1)]

# number = int(input("Enter a number = "))
# l1 = make_list(number)
# l2 = make_list(30)


# print(f"{l1 = }")
# print(f"{l2 = }")


#########################

# more example
check_even = lambda num: num % 2 == 0

print(check_even(100))


###
check_even = lambda num: (
    print("Even") if num % 2 == 0 else print("Odd")
)  # this is also know as ternary operator
check_even(100)
