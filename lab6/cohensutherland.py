import matplotlib.pyplot as plt

# Define the clipping window
x_min = float(input("enter x_min:"))
x_max = float(input("enter x_max:"))
y_min = float(input("enter y_min:"))
y_max = float(input("enter y_max:"))

# Define the line endpoints
x1 = float(input("Enter x1 coordinate of the line:"))# x1 = 100
y1 = float(input("Enter y1 coordinate of the line:"))# y1 = 100
x2 = float(input("Enter x2 coordinate of the line:"))# x2 = 300
y2 = float(input("Enter y2 coordinate of the line:"))# y2 = 300

# Define Cohen-Sutherland codes for the endpoints
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if not (code1 | code2):  # both endpoints inside window
            accept = True
            break
        elif code1 & code2:  # both endpoints outside same side of window
            break
        else:
            x = 0
            y = 0
            if code1:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = compute_code(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = compute_code(x2, y2)

    if accept:
        plt.plot([x1, x2], [y1, y2], color='green')
    else:
        print("Line rejected!")

# Plotting the clipping window
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color='blue')

# Plotting the original line
plt.plot([x1, x2], [y1, y2], color='red')

# Clipping the line
cohen_sutherland(x1, y1, x2, y2)

# Adding some titles and labels because why not
plt.title('Cohen-Sutherland Line Clipping')
plt.xlabel('X')
plt.ylabel('Y')

# Show off your masterpiece
plt.axis('equal')
plt.show()
