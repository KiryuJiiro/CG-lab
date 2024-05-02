#include<graphics.h>
#include<math.h>
int x[4],y[4];
void bezier(int x[4],int y[4])
{
int gd=DETECT,gm,i;

double t,xt,yt;
initgraph(&gd,&gm,"C:\\TC\\BGI");
for(t=0.0;t<1.0;t+=0.0005)
{
xt=pow((1.0-t),3)*x[0]+3*t*pow((1.0-t),2)*x[1]+3*pow(t,2)*(1.0-t)*x[2]+pow(t,3)*x[3];
yt=pow((1.0)-t,3)*y[0]+3*t*pow((1.0)-t,2)*y[1]+3*pow(t,2)*(1.0-t)*y[2]+pow(t,3)*y[3];
putpixel(xt,yt,WHITE);
delay(0);
}
for(i=0;i<4;i++)
{
putpixel(x[i],y[i], YELLOW);
circle(x[i],y[i],YELLOW);
delay(0);
}
getch();
closegraph();
}
int main()
{
int i,x[4],y[4];
printf("Enter the four control points :\n");
for(i=0;i<4;i++)
{
scanf("%d %d",&x[i],&y[i]);
}
bezier(x,y);
}

// 1. Include <graphics.h> and <math.h>.
// 2. Implement 'bezier(x[4], y[4])':
//    a. Initialize graphics.
//    b. Iterate through 't' from 0.0 to 1.0 with steps 0.0005.
//        - Calculate 'xt' and 'yt' using Bezier curve formula.
//        - Draw point (xt, yt) with 'putpixel(xt, yt, WHITE)'.
//        - Delay with 'delay(5)'.
//    c. Draw control points as circles and lines.
//        - Draw points (x[i], y[i]) with 'putpixel(x[i], y[i], WHITE)'.
//        - Draw circles with 'circle(x[i], y[i], 2)'.
//        - Delay with 'delay(2)'.
//    d. Wait for a key press with 'getch' and close graphics.

// 3. Implement 'main':
//    a. Read four control points into arrays 'x[4]' and 'y[4]'.
//    b. Call 'bezier(x, y)'.

// 4. Run the program to draw the Bezier curve and control points.

