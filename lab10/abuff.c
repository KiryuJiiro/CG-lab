#include <stdio.h>
#include <graphics.h>
#include <stdlib.h>

#define WIDTH 800
#define HEIGHT 600

typedef struct {
    int color;
    float alpha;
} PixelData;

void aBufferDrawPixel(int x, int y, int color, float alpha, PixelData* buffer) {
    int index = y * WIDTH + x;

    // If the new pixel has higher opacity, update the buffer
    if (alpha > buffer[index].alpha) {
        buffer[index].color = color;
        buffer[index].alpha = alpha;
        putpixel(x, y, color);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    PixelData* aBuffer = (PixelData*)malloc(sizeof(PixelData) * WIDTH * HEIGHT);

    // Initialize the A-buffer
    for (int i = 0; i < WIDTH * HEIGHT; i++) {
        aBuffer[i].color = BLACK;
        aBuffer[i].alpha = 0.0;
    }

    // Draw two rectangles with varying opacities
    for (int y = 100; y < 200; y++) {
        for (int x = 100; x < 300; x++) {
            aBufferDrawPixel(x, y, RED, 0.5, aBuffer); // Semi-transparent red rectangle
        }
    }

    for (int y = 150; y < 250; y++) {
        for (int x = 200; x < 400; x++) {
            aBufferDrawPixel(x, y, BLUE, 0.7, aBuffer); // Semi-transparent blue rectangle
        }
    }

    // Display the final result on the screen
  getch();
    closegraph();
    return 0;
}

// Initialize A-buffer:

// Create an array of PixelData structures to store color and alpha values for each pixel on the screen.
// Set the color to a default value (e.g., BLACK) and the alpha value to 0.0 for all pixels.
// A-buffer drawing function (aBufferDrawPixel):

// Input: Pixel position (x, y), color, alpha, and the A-buffer array.
// Calculate the index of the pixel in the A-buffer array: index = y * WIDTH + x.
// If alpha > buffer[index].alpha, update the A-buffer:
// buffer[index].color = color (the new color).
// buffer[index].alpha = alpha (the new alpha).
// Draw the pixel on the screen using the updated color.
// Main function:

// Initialize the graphics system.
// Create the A-buffer array using dynamic memory allocation.
// Call the aBufferDrawPixel function to draw objects with varying colors and alpha values, updating the A-buffer for each pixel.
// Display the final result on the screen.
