def circle(radius: float) -> float:
    area = 3.14 * radius * radius
    return area


def rectangle(length: float, breadth: float):
    area = length * breadth
    print("Area of rectange is", area)


def square(side: float):
    area = side**2
    print("Area of square is", area)


def triangle(base: float, height: float):
    area = 0.5 * base * height
    print("Area of triangle is", area)


# why do we use __main__
# the below line will only run when we run this file (define.py)
# but if import this in other file ,this will not run as name == <file_name>
if __name__ == "__main__":
    circle(34)
    square(5)
