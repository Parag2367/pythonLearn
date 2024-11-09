import threading


def print_using_for(num):
    for i in range(1, num + 1):
        print(i, "FOR")


def print_using_while(num):
    i = 1
    while i <= num:
        print(i, "WHILE")
        i += 1


t1 = threading.Thread(target=print_using_for, args=(1000,))
t2 = threading.Thread(target=print_using_while, args=(1000,))
t1.start()
t2.start()

# t1.join()
# t2.join()
