#include <stdio.h>
#include <math.h>
#include <graphics.h>

void draw(int,int,int,int,int);
void trans(int,int,int,int,int);
void initialize(int*,int*,int*,int*,int*);

int main()
{
    int gd = DETECT, gm, c;
    initgraph(&gd, &gm, "");
    int x1, y1, x2, y2, depth;
    initialize(&x1, &y1, &x2, &y2, &depth);

   draw(x1, y1, x2, y2, depth);
   // getch();
    //cleardevice();
    trans(x1, y1, x2, y2, depth);
    getch();

    closegraph();
    return 0;
}

void draw(int x1, int y1, int x2, int y2, int depth)
{
    bar3d(x1, y1, x2, y2, depth, 1);
}

void trans(int x1, int y1, int x2, int y2, int depth)
{
    int a1, a2, b1, b2, dep, x, y;
    printf("Enter the translation distances:\n");
    scanf("%d%d", &x, &y);

    a1 = x1 + x;
    a2 = x2 + x;
    b1 = y1 + y;
    b2 = y2 + y;
    dep = abs(a2 - a1) / 4;

    bar3d(a1, b1, a2, b2, dep, 1);
    setcolor(5);
    draw(a1, b1, a2, b2, dep);
}

void initialize(int *x1, int *y1, int *x2, int *y2, int *depth)
{
    printf("Enter 1st top value (x1, y1):\n");
    scanf("%d%d", x1, y1);
    printf("Enter right bottom value (x2, y2):\n");
    scanf("%d%d", x2, y2);

    *depth = abs(*x2 - *x1) / 4;
}
//  Define the coordinates (x1, y1) of the top-left corner and (x2, y2) of the bottom-right corner of the 3D cube.
// Calculate the depth of the cube as (depth = (x2 - x1) / 4).
// Draw the original 3D cube using the draw function.
// Get the user input for the translation distances along the x and y axes (x and y).
// Calculate the new coordinates of the translated cube:
// a1 = x1 + x
// a2 = x2 + x
// b1 = y1 + y
// b2 = y2 + y
// dep = abs(a2 - a1) / 4 (to maintain the original depth).
// Draw the translated 3D cube using the bar3d function and set the color to 5 for visual distinction.
// Redraw the original 3D cube using the draw function to keep the original object visible on the screen.
// Close the graphics window and end the program.

