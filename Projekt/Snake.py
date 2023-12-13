from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 20
BODY_PARTS = 5
SNAKE_COLOR = "#0863F9"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#19AE0D"

def start():
    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.place(x=0,y=0)

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    window.update()

    class Snake:

        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0, BODY_PARTS):
                self.coordinates.append([0, 0])

            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
                self.squares.append(square)

    class Food:

        def __init__(self):

            x = random.randint(0, (GAME_WIDTH//SPACE_SIZE)-1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT//SPACE_SIZE)-1) * SPACE_SIZE

            self.coordinates = [x, y]

            canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


    def next_turn(snake, food):

        x, y = snake.coordinates[0]

        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

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
            window.after(SPEED, next_turn, snake, food)


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

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False


    def game_over():

        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                        font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")
    
    snake = Snake()
    food = Food()

    next_turn(snake, food)


window = Tk()
window.title("Snake game")

canvas_start = Canvas(window, bg='#FF00FF', height=GAME_HEIGHT, width=GAME_WIDTH)
canvas_start.pack()

def place_button_center():
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    button_width = 200
    button_height = 200
    x = (window_width - button_width) / 2
    y = (window_height - button_height) / 2
    b.place(x=x, y=y)

b = Button(window, text='START', height='10', width='20', bd='20', command=start)
b.place(x=0, y=0)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

direction = 'down'

def change_direction(new_direction):
    global direction
    if new_direction in ['left', 'right', 'up', 'down']:
        direction = new_direction

def set_key_bindings():
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

score = 0

set_key_bindings()
place_button_center()

window.mainloop()