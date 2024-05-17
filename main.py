from sys import exit
from turtle import Turtle, Screen
from tkinter import messagebox
import random

# Basic config (do not edit)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITIONS = [-70, -40, -10, 20, 50, 80]
STARTING_X_POSITION = -230
FINISHING_X_POSITION = 230
ALL_TURTLES = []
screen = Screen()
screen.setup(500, 400)
screen.title("Turtle race")
screen.bgcolor("black")


def get_user_input():
    """
    Gets the user input on which turtle will win
    :return: the user choice, if valid
    """
    user_bet = ""
    while user_bet.lower() not in COLORS:
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter your color?")
        if user_bet.lower() in COLORS:
            return user_bet
        else:
            messagebox.showinfo("Invalid input", "Enter a valid color.")


def create_turtles():
    """
    Create the turtles and finishing line on the screen
    """
    for turtle_index in range(0, 6):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(COLORS[turtle_index])
        t.goto(STARTING_X_POSITION, Y_POSITIONS[turtle_index])
        ALL_TURTLES.append(t)

    finishing_line = Turtle(shape="turtle")
    finishing_line.penup()
    finishing_line.color("white")
    finishing_line.goto(FINISHING_X_POSITION, -100)
    finishing_line.pendown()
    finishing_line.setheading(90)
    finishing_line.forward(220)


def race_the_turtles():
    """
    The function responsible for racing the turtles
    :return: The color of the winning turtle
    """
    while True:
        for t in ALL_TURTLES:
            if t.xcor() > FINISHING_X_POSITION:
                return t.pencolor()
            random_distance = random.randint(0, 10)
            t.forward(random_distance)


def display_result(user_choice, winner):
    """
    Displays information if you won or lost and asks if the user wants to play again
    :param user_choice: The turtle color user bet on
    :param winner: The color of the winning turtle
    """
    if winner == user_choice:
        messagebox.showinfo("You win", f"The {winner} turtle is the winner!")
    else:
        messagebox.showinfo("You lost", f"The {winner} turtle is the winner!")
    if messagebox.askyesno("Turtle Game", "Do you want to play again?"):
        host_turtle_race()
    else:
        exit(0)


def reset_screen():
    """
    Clears the screen and game information
    """
    screen.clear()
    screen.bgcolor("black")
    global ALL_TURTLES
    ALL_TURTLES = []


def host_turtle_race():
    """
    Driver function of running the turtle race
    """
    reset_screen()
    user_choice = get_user_input()
    create_turtles()
    winner = race_the_turtles()
    display_result(user_choice, winner)


if __name__ == '__main__':
    host_turtle_race()
    screen.exitonclick()
