import math
import numpy as np
import matplotlib.pyplot as plt

x1 = float(input("Enter x1 co-ordinate:"))
y1 = float(input("Enter y1 co-ordinate:"))
x2 = float(input("Enter x2 co-ordinate:"))
y2 = float(input("Enter y2 co-ordinate:"))
x3 =float(input("Enter x3 co-ordinate:"))
y3 =float(input("Enter y3 co-ordinate:"))

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)

plt.plot([x1,x2],[y1,y2])
plt.plot([x2,x3],[y2,y3])
plt.plot([x1,x3],[y1,y3])

theta = float(input("Enter rotating angle:"))
theta = math.radians(theta)
direction = input("""Enter 
                  1)C for clockwise rotation
                  2)A for anticlockwise rotation
                  """)
sin = math.sin(theta)
cos = math.cos(theta)

if direction == "A":
    x1d = x1 * cos - y1 * sin
    y1d = x1 * sin + y1 * cos
    x2d = x2 * cos - y2 * sin
    y2d = x2 * sin + y2 * cos
    x3d = x3 * cos - y3 * sin
    y3d = x3 * sin + y3 * cos
else:
    x1d = x1 * cos + y1 * sin
    y1d = -x1 * sin + y1 * cos
    x2d = x2 * cos + y2 * sin
    y2d = -x2 * sin + y2 * cos
    x3d = x3 * cos + y3 * sin
    y3d = -x3 * sin + y3 * cos

plt.scatter(x1d, y1d)
plt.scatter(x2d, y2d)
plt.scatter(x3d, y3d)

plt.plot([x1d,x2d],[y1d,y2d])
plt.plot([x2d,x3d],[y2d,y3d])
plt.plot([x1d,x3d],[y1d,y3d])
print("Coodinates after rotation:")
print(f"[{round(x1d,2)}, {round(y1d,2)}], [{round(x2d,2)}, {round(y2d,2)}]")
print(f"[{round(x2d,2)}, {round(y2d,2)}], [{round(x3d,2)}, {round(y3d,2)}]")
print(f"[{round(x3d,2)}, {round(y3d,2)}], [{round(x1d,2)}, {round(y1d,2)}]")


plt.show()