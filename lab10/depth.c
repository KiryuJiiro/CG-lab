#include <stdio.h>
#include <graphics.h>
#include <stdlib.h>
#include <math.h>

#define WIDTH 800
#define HEIGHT 600

void drawScene(int x1, int y1, int x2, int y2, int depth) {
    int color = WHITE;
    for (int y = y1; y <= y2; y++) {
        for (int x = x1; x <= x2; x++) {
            // Simulate a depth value (in this example, we use the y-coordinate)
            int z = y * 100 / HEIGHT;

            if (z < depth) {
                putpixel(x, y, color);
            }
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Simulate two objects with different depths
    drawScene(100, 100, 300, 400, 10); // Object 1 with depth 10
    drawScene(200, 200, 400, 500, 50); // Object 2 with depth 50

getch();
    closegraph();
    return 0;
}
