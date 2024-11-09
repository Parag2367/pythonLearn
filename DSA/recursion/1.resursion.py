count = 1


def rec():
    global count
    print(count)
    if count == 5:
        return
    count += 1
    rec()


if __name__ == "__main__":
    rec()
