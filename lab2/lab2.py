import matplotlib.pyplot as plt
import math

x1 = float(input("Enter starting co-ordinate x1:"))
y1 = float(input("Enter starting co-ordinate y1:"))
x2 = float(input("Enter ending co-ordinate x2:"))
y2 = float(input("Enter ending co-ordinate y2:"))

dx = x2-x1
dy = y2-y1

xk = x1
yk = y1
m = dy/dx
plt.plot([x1,x2],[y1,y2])
if m<1:
    steps = int(abs(dx))
else:
    steps = int(abs(dy))

xincr = dx/float(steps)
yincr = dy/float(steps)
i = 0
print("iteration\t xk\t\t yk\t (xk+1,yk+1)")
while(i < steps):
    plt.scatter(round(xk),round(yk))
    print(f"{i}\t\t{round(xk,2)}\t\t {round(yk,2)}\t({round(xk)},{round(yk)})")
    i = i + 1
    xk += xincr
    yk += yincr
print("Name : Aditya Pokhrel")
print("Roll no : 3")
plt.show()


