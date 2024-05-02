import turtle

def draw_polygon(vertices):
    turtle.penup()
    turtle.goto(vertices[0])
    turtle.pendown()

    for vertex in vertices[1:]:
        turtle.goto(vertex)

    turtle.goto(vertices[0])  # Close the loop

def find_min_max_x(vertices):
    x_values = [vertex[0] for vertex in vertices]
    return min(x_values), max(x_values)

def scanline_fill(vertices):
    min_x, max_x = find_min_max_x(vertices)

    for y in range(int(min(vertices, key=lambda x: x[1])[1]), int(max(vertices, key=lambda x: x[1])[1]) + 1):
        x_intercepts = []

        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]

            if (y1 <= y < y2) or (y2 <= y < y1):
                x = x1 + (y - y1) / (y2 - y1) * (x2 - x1)
                x_intercepts.append(x)

                x_intercepts.sort()

        for i in range(0, len(x_intercepts), 2):
            turtle.penup()
            turtle.goto(x_intercepts[i], y)
            turtle.pendown()
            turtle.forward(x_intercepts[i + 1] - x_intercepts[i])

def main():
    turtle.speed(0)

    # Example vertices of a triangle
    triangle_vertices = [(-100, -100), (0, 100), (100, -100)]

    draw_polygon(triangle_vertices)
    scanline_fill(triangle_vertices)

    turtle.mainloop()

if __name__ == "__main__":
    main()
