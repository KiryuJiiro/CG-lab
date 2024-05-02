import math
import matplotlib.pyplot as plt

x1 =float(input("enter the first coordinate x1:"))
y1 =float(input("enter the second coordinate y1:"))
x2 =float(input("enter the another x coordinate x2:"))
y2 =float(input("enter the another y coordinate y2"))
plt.scatter(x1,y1)
plt.scatter(x2,y2)

plt.plot([x1,x2],[y1,y2])
plt.scatter(x1,y1)

tx =float(input("by what x coordinate we need to translate it as tx:"))
ty =float(input("by what y coordinate we need to translate it as ty:"))

tx1 = tx+x1;
ty1 = ty+y1;
tx2 = tx+x2;
ty2 = ty+y2;

print("Translated coordinates:")
print(f"X-coordinates:({tx1},{tx2})")
print(f"y-coordinates:({ty1},{ty2})")
plt.scatter(tx1,ty1)
plt.scatter(tx2,ty2)
plt.plot([tx1,tx2],[ty1,ty2])
plt.show()
