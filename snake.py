from tkinter import *
import random

# Not working because of course it fricking isnt 💀

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"


class Snake:
    pass


class Food:
    pass


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collisions():
    pass


def game_over():
    pass


window = Tk()
window.title("Snek gaem") # .title() lets you... set the title of the window!
window.resizable(False, False) # this means you cant make the window bigger by dragging with mouse. it's kinda wierd that you need to put False twice

score = 0
direction = "down"

label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

window.mainloop()
