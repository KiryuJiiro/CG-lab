import math
import matplotlib.pyplot as plt

def X(x1, y1, x2, y2, x3, y3):
    y1 = -y1
    y2 = -y2
    y3 = -y3
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x2, x3], [y2, y3])
    plt.plot([x3, x1], [y3, y1])
    print("Coodinates after reflection:")
    print(f"[{x1}, {y1}], [{x2}, {y2}]")
    print(f"[{x2}, {y2}], [{x3}, {y3}]")
    print(f"[{x3}, {y3}], [{x1}, {y1}]")
    plt.show()

def Y(x1, y1, x2, y2, x3, y3):
    x1 = -x1
    x2 = -x2
    x3 = -x3
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x2, x3], [y2, y3])
    plt.plot([x3, x1], [y3, y1])
    print("Coodinates after reflection:")
    print(f"[{x1}, {y1}], [{x2}, {y2}]")
    print(f"[{x2}, {y2}], [{x3}, {y3}]")
    print(f"[{x3}, {y3}], [{x1}, {y1}]")
    plt.show()

def slope(x1, y1, x2, y2, x3, y3):
    c = float(input("Enter y-intercept:"))
    m = float(input("Enter slope:"))
    angle = 1 / math.tan(m)
    theta = angle
    theta = math.radians(theta)

    y1 = y1 - c
    y2 = y2 - c
    y3 = y3 - c

    sin = math.sin(theta)
    cos = math.cos(theta)

    x1 = x1 * cos + y1 * sin
    y1 = -x1 * sin + y1 * cos
    x2 = x2 * cos + y2 * sin
    y2 = -x2 * sin + y2 * cos
    x3 = x3 * cos + y3 * sin
    y3 = -x3 * sin + y3 * cos

    y1 = -y1
    y2 = -y2
    y3 = -y3

    x1 = x1 * cos - y1 * sin
    y1 = x1 * sin + y1 * cos
    x2 = x2 * cos - y2 * sin
    y2 = x2 * sin + y2 * cos
    x3 = x3 * cos - y3 * sin
    y3 = x3 * sin + y3 * cos

    y1 = y1 + c
    y2 = y2 + c
    y3 = y3 + c

    plt.plot([x1, x2], [y1, y2])
    plt.plot([x2, x3], [y2, y3])
    plt.plot([x3, x1], [y3, y1])
    print("Coodinates after reflection:")
    print(f"[{x1}, {y1}], [{x2}, {y2}]")
    print(f"[{x2}, {y2}], [{x3}, {y3}]")
    print(f"[{x3}, {y3}], [{x1}, {y1}]")
    plt.show()

def switch_case(choice, arguments):
    switch_dict = {
        'X': X,
        'Y': Y,
        'slope': slope
    }
    func = switch_dict.get(choice)
    if func:
        func(*arguments)
    else:
        print("Invalid choice")

# Making a triangle
x1 = float(input("Enter x1 coordinate:"))
y1 = float(input("Enter y1 coordinate:"))

x2 = float(input("Enter x2 coordinate:"))
y2 = float(input("Enter y2 coordinate:"))

x3 = float(input("Enter x3 coordinate:"))
y3 = float(input("Enter y3 coordinate:"))

plt.plot([x1, x2], [y1, y2])
plt.plot([x2, x3], [y2, y3])
plt.plot([x3, x1], [y3, y1])

# Rotation starts
choice = input("Enter type of rotation (X, Y, slope): ")
arguments = (x1, y1, x2, y2, x3, y3)

switch_case(choice, arguments)
