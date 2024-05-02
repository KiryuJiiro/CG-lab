import pandas as pd
import matplotlib.pyplot as plt
import math

def plotcircle(n, xs, ys):
    data = {"(x, y)": [(x, y) for x, y in zip(xs, ys)],
            "(x, -y)": [(x, -y) for x, y in zip(xs, ys)],
            "(y, -x)": [(y, -x) for x, y in zip(xs, ys)],
            "(-y, -x)": [(-y, -x) for x, y in zip(xs, ys)],
            "(-x, -y)": [(-x, -y) for x, y in zip(xs, ys)],
            "(-x, y)": [(-x, y) for x, y in zip(xs, ys)],
            "(-y, x)": [(-y, x) for x, y in zip(xs, ys)],
            "(y, x)": [(y, x) for x, y in zip(xs, ys)]}

    df = pd.DataFrame(data)
    print(df)

    for col in df.columns:
        plt.scatter(df[col].apply(lambda x: x[0]), df[col].apply(lambda x: x[1]))

def main():
    r = float(input("Enter radius: "))
    shift_x, shift_y = map(float, input("Enter x and y: ").split())

    p0 = 1 - r
    x, y = 0, r
    xs, ys = [], []

    while x < y:
        if p0 < 0:
            x += 1
            p0 = p0 + 2 * x + 1
        else:
            x += 1
            y -= 1
            p0 = p0 + 2 * x + 1 - 2 * y

        xs.append(x + shift_x)
        ys.append(y + shift_y)

    steps = len(xs)
    print("\n", steps, "\n")
    plotcircle(steps, xs, ys)

if __name__ == "__main__":
    main()

plt.show()
