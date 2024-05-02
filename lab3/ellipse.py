import matplotlib.pyplot as plt
import pandas as pd

rx = float(input("Enter the radius of the x-axis: "))
ry = float(input("Enter the radius of the y-axis: "))
x = 0
y = ry
xk = x
yk = y
pnot = rx * rx * ry + (1/4) * rx * rx
pk = pnot

data = {"Quadrant 1": [], "Quadrant 2": [], "Quadrant 3": [], "Quadrant 4": []}

# First quadrant
while 2 * ry * ry * xk < 2 * rx * rx * yk:
    if pk < 0:
        xk += 1
        pk += 2 * ry * ry * xk
    else:
        xk += 1
        yk -= 1
        pk += 2 * ry * ry * xk - 2 * rx * rx * yk

    data["Quadrant 1"].append((xk, yk))
    data["Quadrant 2"].append((-xk, yk))
    data["Quadrant 3"].append((-xk, -yk))
    data["Quadrant 4"].append((xk, -yk))

# Now for the second region
xk2 = xk
yk2 = yk
p20 = ry * ry * (xk2 + (1/2))**2 + rx * rx * (yk2 - 1)**2 - rx**2 * ry**2

# Second quadrant
while yk2 != 0:
    if p20 > 0:
        yk2 -= 1
        p20 -= 2 * rx * rx * yk2 + rx * rx
    else:
        xk2 += 1
        yk2 -= 1
        p20 += -2 * rx * rx * yk2 + rx * rx + 2 * ry * ry * xk2

    data["Quadrant 1"].append((xk2, yk2))
    data["Quadrant 2"].append((-xk2, yk2))
    data["Quadrant 3"].append((-xk2, -yk2))
    data["Quadrant 4"].append((xk2, -yk2))

df = pd.DataFrame(data)
print(df)

for col in df.columns:
    for coord in df[col]:
        plt.scatter(coord[0], coord[1])

plt.show()
