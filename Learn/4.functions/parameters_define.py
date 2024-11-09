def addition(n1, n2):  # n1,n2 are parameters
    sum = n1 + n2
    print(sum)


addition(20, 30)  # 20,30 are parameters


# example 2
def addition_list(x):
    total = 0
    for a in x:
        total = total + a
    print(total)


my_list = [2, 34, 54, 67, 88]
addition_list(my_list)
