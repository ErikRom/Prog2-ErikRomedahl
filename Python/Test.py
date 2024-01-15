from tkinter import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 250
SPACE_SIZE = 20
BODY_PARTS = 5
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

window = Tk()
window.title("Snake game")
window.resizable(False, False)
window.geometry('500x500')

canvas_start = Canvas(window, bg='#FF00FF', height=500, width=500)
canvas_start.pack()

b = Button(window, text='START')
b.pack()

window.update()

window.mainloop()