def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"Area of circle with radius {radius} = {area}")


def rectange(length: float, breadth: float) -> None:
    area = length * breadth
    print(f"Area of rectangle = {area}")


def triangle(base: float, height: float) -> None:
    area = 0.5 * height * base
    print(f"Area of triangle = {area}")


if __name__ == "__main__":
    circle(43.55)
    triangle(100, 55)
