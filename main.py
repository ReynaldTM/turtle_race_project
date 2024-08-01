import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ["red", "green", "blue", "orange", "yellow", "black", "cyan", "pink", "brown", "purple"]


def get_number_racers():
    racers = 0  # I think this is redundant
    while True:
        racers = input("How many turtles do you want to race? (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric.  Try again!")
            continue

        if 2 <= racers <= 10:  # checking 2 is less than or equal than racer, racer is less than or equal to 10
            return racers
        else:
            print("Number not in range 2-10.  Try again!")


def race(colors):
    turtles = create_turtles(colors)
    winner_position = 0

    while True:  # will continue until a turtle finishes
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    # noinspection SpellCheckingInspection
    spacingx = WIDTH // (len(colors) + 1)  # for spacing turtles
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        # -250/2 + INDEX OF RACER + 1 for x-axis.  -250/2 + 20 for y-axis position
        racer.pendown()
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = get_number_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)

print(f"The winner is the turtle with color {winner}!")
time.sleep(5)
