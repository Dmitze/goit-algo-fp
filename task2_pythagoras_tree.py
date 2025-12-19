import turtle
import math


def draw_tree(branch, angle, depth, x, y):
    if depth == 0:
        return

    end_x = x + branch * math.cos(math.radians(angle))
    end_y = y + branch * math.sin(math.radians(angle))

    turtle.pensize(depth)
    turtle.pencolor("brown" if depth > 2 else "green")
    
    turtle.goto(x, y)
    turtle.goto(end_x, end_y)

    draw_tree(branch * 0.7, angle - 30, depth - 1, end_x, end_y)
    draw_tree(branch * 0.7, angle + 30, depth - 1, end_x, end_y)


def setup_canvas(width, height):
    turtle.setup(width=width, height=height)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()


def main():
    setup_canvas(800, 600)
    
    depth = int(input("Введіть рівень рекурсії (1-15): "))
    
    if depth < 1 or depth > 15:
        depth = 10
    
    draw_tree(100, 90, depth, 0, -200)
    
    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
