#------------------------------LIBRARIES-----------------------------#
from tkinter import *
import random
from tkinter import colorchooser

#------------------------------FUNCTIONS-----------------------------#

def start():
    global direction
    global score
    direction = 'down'
    score = 0

    canvas = Canvas(window, bg=background_color, height=game_height, width=game_width)
    canvas.place(x=0, y=0)

    canvas_top = Canvas(window, bg=('#000000'), height=60, width=game_width)
    canvas_top.place(x=0, y=0)

    label = Label(window, text="Score:{}".format(score), bg='#000000', fg='#FFFFFF', font=('consolas', 25))
    label.place(x=10, y=10)

    label_highscore = Label(window, text="Highscore:{}".format(highscore), bg='#000000', fg='#FFFFFF',
                            font=('consolas', 25))
    label_highscore.place(x=350, y=10)

    label_highscore = Label(window, text="Highscore:{}".format(highscore), bg='#000000', fg='#FFFFFF', font=('consolas', 25))
    label_highscore.place(x=350, y=10)
    
    window.update()
    

    class Snake:

        def __init__(self):
            self.body_size = body_parts
            self.coordinates = []
            self.squares = []

            for i in range(0, body_parts):
                self.coordinates.append([0, 2*space_size])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="snake")
                self.squares.append(square)


    class Food:
        global Food

        def __init__(self):
            x = random.randint(0, (game_width // space_size) - 1) * space_size
            y = random.randint(2, (game_height // space_size) - 1) * space_size
            print(y)
            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")

    def next_turn(snake, food):
        x, y = snake.coordinates[0]

        if direction == "up":
            y -= space_size
        elif direction == "down":
            y += space_size
        elif direction == "left":
            x -= space_size
        elif direction == "right":
            x += space_size

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:

            global score

            score += 1

            label.config(text="Score:{}".format(score))

            canvas.delete("food")

            food = Food()

        else:

            del snake.coordinates[-1]

            canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        if check_collisions(snake):
            game_over()

        else:
            window.after(speed, next_turn, snake, food)

    def change_direction(new_direction):
        global direction

        if new_direction == 'left':
            if direction != 'right':
                direction = new_direction
        elif new_direction == 'right':
            if direction != 'left':
                direction = new_direction
        elif new_direction == 'up':
            if direction != 'down':
                direction = new_direction
        elif new_direction == 'down':
            if direction != 'up':
                direction = new_direction

    def check_collisions(snake):
        x, y = snake.coordinates[0]
        
        if x < 0 or x >= game_width:
            return True
        elif y < label_height or y >= game_height:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over():
        global score
        global highscore

        if score > highscore:
            highscore = score

        canvas.destroy()

        canvas_gameover = Canvas(window, bg='#ADD8E6', height=game_height, width=game_width)
        canvas_gameover.place(x=0, y=0)

        canvas_gameover.create_text(350, 100, font=('Helvetica', 70), text="GAME OVER", fill="red")

        b = Button(window, text="RESTART", height='5', width='20', command=start)
        b.place(x=window_width / 2 - 70, y=350)

        bu = Button(window, text='MENU', height='5', width='20', command=menu)
        bu.place(x=window_width / 2 - 70, y=500)

        label_highscore.config(text="Highscore:{}".format(highscore))

        window.update()

    def set_key_bindings():
        window.bind('<a>', lambda event: change_direction('left'))
        window.bind('<d>', lambda event: change_direction('right'))
        window.bind('<w>', lambda event: change_direction('up'))
        window.bind('<s>', lambda event: change_direction('down'))
        
        window.bind('<Left>', lambda event: change_direction('left'))
        window.bind('<Right>', lambda event: change_direction('right'))
        window.bind('<Up>', lambda event: change_direction('up'))
        window.bind('<Down>', lambda event: change_direction('down'))

    set_key_bindings()
    snake = Snake()
    food = Food()

    next_turn(snake, food)


def menu():
    canvas_start = Canvas(window, bg='#ADD8E6', height=game_height, width=game_width)
    canvas_start.place(x=0, y=0)

    canvas_start.create_text(350, 100, font=('consalolas', 70), text='SNAKE', fill="#0863F9")
    canvas_start.create_text(350, 650, font=('consalolas', 10), text='Av Erik Romedahl och Jack Forsman',
                             fill="#000000")

    canvas_start.create_text(195, 525, font=('consalolas', 15), text='Snake speed',
                             fill="#000000")
    canvas_start.create_text(500, 525, font=('consalolas', 15), text='Map size',
                             fill="#000000")

    b_food = Button(window, text='FOOD COLOR', height='5', width='20', command=Foodcolor)
    b_food.place(x=260, y=400)

    b_background = Button(window, text='BACKGROUND COLOR', height='5', width='20', command=Backgroundcolor)
    b_background.place(x=100, y=400)

    b_snake = Button(window, text='SNAKE COLOR', height='5', width='20', command=Snakecolor)
    b_snake.place(x=420, y=400)

    b_snake = Button(window, text='Slow', height='2', width='10', command=lambda: set_speed(150))
    b_snake.place(x=80, y=540)

    b_snake = Button(window, text='Normal', height='2', width='10', command=lambda: set_speed(100))
    b_snake.place(x=160, y=540)

    b_snake = Button(window, text='Fast', height='2', width='10', command=lambda: set_speed(50))
    b_snake.place(x=240, y=540)

    b_snake = Button(window, text='Small', height='2', width='10', command=lambda: set_size(69))
    b_snake.place(x=385, y=540)

    b_snake = Button(window, text='Normal', height='2', width='10', command=lambda: set_size(30))
    b_snake.place(x=465, y=540)

    b_snake = Button(window, text='Large', height='2', width='10', command=lambda: set_size(23))
    b_snake.place(x=545, y=540)

    b = Button(window, text='PLAY', height='5', width='20', command=start)
    b.place(x=260, y=280)

    window.update()


def Foodcolor():
    global food_color
    food_color = colorchooser.askcolor()[1]
    menu()

def Backgroundcolor():
    global background_color
    background_color = colorchooser.askcolor()[1]
    menu()

def Snakecolor():
    global snake_color
    snake_color = colorchooser.askcolor()[1]
    menu()

def set_speed(new_speed):
    global speed
    speed = new_speed

def set_size(new_size):
    global space_size
    space_size = new_size


# ---------------------------DEFINED VALUES---------------------------#
game_width = 690
game_height = 690
speed = 50
space_size = 30
body_parts = 5
snake_color = "#0863F9"
food_color = "#FF0000"
background_color = "#19AE0D"
score = 0
highscore = 0
label_height = 60

# --------------------------------------------------------------------#

# -------------------------START OF PROGRAM---------------------------#
window = Tk()
window.title("Snake game")

canvas_start = Canvas(window, bg='#ADD8E6', height=game_height, width=game_width)
canvas_start.pack()

menu()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()

# --------------------------------------------------------------------#
