from tkinter import *
import random

root = Tk()
root.title("Snake Game")

Label(root, text="Snake by Erik and Jack").pack(side=BOTTOM)
b = Button(root, text="START").pack()

def click_handler(self):
    game()

b.bind("<Button-1>", click_handler)

def game():
    game_width = 400
    game_height = 400
    score = 0
    speed = 100
    direction = "down"
    space_size = 30
    body_parts = 3
    snake_color = "#8AAAE5"
    food_color = "#FF0000"
    background_color = "#FFFFFF"

    label = Label(root, text="Score: {}".format(score)).pack()

    canvas = Canvas(root, bg=background_color, height=game_height, width=game_width).pack()

    class Snake:
        def __init__(self, length, color):
            self.length = length
            self.color = color


    class Food:
        def __init__(self, points):
            self.points = points

root.geometry("500x500+250+250")
root.mainloop() 