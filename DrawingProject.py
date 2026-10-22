import turtle


def draw_rectangle(t, x, y, width, height, colour):
    """Draw a rectangle starting at its bottom-left corner."""
    t.up()
    t.goto(x, y)
    t.color("black")
    t.fillcolor(colour)
    t.pensize(1)
    t.down()
    t.begin_fill()

    for side in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()
    t.up()


def draw_mountain(t, x, y, colour):
    """Draw a simple triangle-shaped mountain."""
    t.up()
    t.goto(x, y)
    t.color("black")
    t.fillcolor(colour)
    t.down()
    t.begin_fill()
    t.goto(x + 80, y + 70)
    t.goto(x + 160, y)
    t.goto(x, y)
    t.end_fill()
    t.up()


def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.setworldcoordinates(-360, -240, 360, 240)

    alex = turtle.Turtle()
    alex.speed(0)
    alex.shape("blank")

    # Sun and mountains.
    alex.up()
    alex.goto(-240, 160)
    alex.color("yellow")
    alex.dot(55)

    draw_mountain(alex, -330, 60, "slategray")
    draw_mountain(alex, -225, 60, "lightgray")

    # Ocean and a strip of sandy beach.
    draw_rectangle(alex, -330, -220, 660, 280, "turquoise")
    draw_rectangle(alex, -330, -180, 660, 92, "wheat")

    # Main house and a wooden section on the right.
    draw_rectangle(alex, -150, -90, 250, 130, "lightgray")
    draw_rectangle(alex, 100, -90, 95, 130, "tan")

    # Lines to represent wooden boards.
    for board in range(6):
        x = 108 + board * 15
        alex.up()
        alex.goto(x, -90)
        alex.color("brown")
        alex.down()
        alex.goto(x, 40)
    alex.up()

    # Flat roof and a concrete base.
    draw_rectangle(alex, -165, 40, 375, 15, "dimgray")
    draw_rectangle(alex, -170, -100, 390, 10, "gray")

    # Three large windows.
    for window in range(3):
        x = -135 + window * 75
        draw_rectangle(alex, x, -65, 60, 85, "lightblue")

    # Door and door handle.
    draw_rectangle(alex, 128, -90, 40, 90, "saddlebrown")
    alex.goto(159, -46)
    alex.color("yellow")
    alex.dot(4)

    # Small pond and three stepping stones.
    draw_rectangle(alex, -290, -120, 80, 20, "lightblue")
    for stone in range(3):
        x = -285 + stone * 28
        draw_rectangle(alex, x, -146, 20, 10, "gray")

    # A basic tree: a brown trunk and a green top.
    draw_rectangle(alex, 260, -105, 12, 70, "brown")
    alex.goto(266, -15)
    alex.color("green")
    alex.dot(60)

    # A few straight lines for waves beside the house.
    for wave in range(4):
        y = 35 - wave * 25
        alex.up()
        alex.goto(-315, y)
        alex.color("white")
        alex.down()
        alex.goto(-270, y)
    alex.up()

    screen.exitonclick()


main()
