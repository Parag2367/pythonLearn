def my_func(num):
    print(num)
    if num == 1:
        return
    my_func(num - 1)


my_func(10)
