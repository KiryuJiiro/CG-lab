import math
import matplotlib.pyplot as plt

x1 = float(input("enter x1 point:"))
y1 = float(input("enter y1 point:"))
x2 = float(input("enter x2 point:"))
y2 = float(input("enter y2 point:"))
x3 = float(input("enter x3 point:"))
y3 = float(input("enter y3 point:"))
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)

plt.plot([x1,x2],[y1,y2])
plt.plot([x2,x3],[y2,y3])
plt.plot([x1,x3],[y1,y3])

sx = float(input("enter shearing value for x axis:"))
sy = float(input("enter value for shearing by y axis:"))

choice = input("""
Enter:
1)X for xaxis
2)Y for yaxis
3)XY for xyaxis""")
if choice=="X":
    sx1= x1+y1*sx
    sy1=y1
    sx2= x2+y2*sx
    sy2=y2
    sx3= x3+y3*sx
    sy3=y3
elif choice=="Y":
    sy1= x1*sy+y1
    sx1=x1
    sy2= x2*sy+y2
    sx2=x2
    sy3= x3*sy+y3
    sx3=x3
else:
    sx1= x1+y1*sx
    sx2= x2+y2*sx
    sx3= x3+y3*sx
    sy1= x1*sy+y1
    sy2= x2*sy+y2
    sy3= x3*sy+y3
    

plt.scatter(sx1, sy1)
plt.scatter(sx2, sy2)
plt.scatter(sx3, sy3)

plt.plot([sx1,sx2],[sy1,sy2])
plt.plot([sx2,sx3],[sy2,sy3])
plt.plot([sx1,sx3],[sy1,sy3])
print("Coodinates after shearing:")
print(f"[{sx1}, {sy1}], [{sx2}, {sy2}]")
print(f"[{sx2}, {sy2}], [{sx3}, {sy3}]")
print(f"[{sx3}, {sy3}], [{sx1}, {sy1}]")

plt.show()

    

