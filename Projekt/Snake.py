from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 5
SNAKE_COLOR = "#0863F9"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#19AE0D"

def start():
    score = 0

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT-50, width=GAME_WIDTH)
    canvas.place(x=0,y=60)

    canvas_top = Canvas(window, bg=('#000000'), height=60, width=GAME_WIDTH)
    canvas_top.place(x=0, y=0)

    label = Label(window, text="Score:{}".format(score), bg='#000000', fg='#FFFFFF', font=('consolas', 25))
    label.place(x=10, y=10)

    lable_highscore = Label(window, text="Highscore:{}".format(highscore), bg='#000000', fg='#FFFFFF', font=('consolas', 25))
    lable_highscore.place(x=350, y=10)
    
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
        global highscore

        if score > highscore:
            highscore = score

        canvas.destroy()

        canvas_gameover = Canvas(window, bg='#FF00FF', height=GAME_HEIGHT, width=GAME_WIDTH)
        canvas_gameover.place(x=0,y=0)

        canvas_gameover.create_text(350, 100, font=('Helvetica',70), text="GAME OVER", fill="red")
        
        b = Button(window, text="RESTART", height='5', width='20', command=start)
        b.place(x=window_width/2-70, y=350)
        
        bu = Button(window, text='MENU', height='5', width='20', command=menu)
        bu.place(x=window_width/2-70, y=500)
    
    snake = Snake()
    food = Food()

    next_turn(snake, food)


def menu():
    canvas_start = Canvas(window, bg='#FF00FF', height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas_start.place(x=0,y=0)

    canvas_start.create_text(350, 100, font=('consalolas', 70), text='SNAKE', fill="#0863F9")
    canvas_start.create_text(350, 650, font=('consalolas', 10), text='Av Erik Romedahl och Jack Forsman', fill="#000000")

    b_food = Button(window, text='FOOD COLOR', height='5', width='20', command=food_color)
    b_food.place(x=260, y=400)

    b = Button(window, text='PLAY', height='5', width='20', command=start)
    b.place(x=260, y=280)

    window.update()


def food_color():
    canvas_food = Canvas(window, bg='#FF00FF', height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas_food.place(x=0,y=0)
    
    b_blue = Button(window, text='BLUE', height='5', width='20', command=menu)
    b_blue.place(x=280, y=280)


def change_direction(new_direction):
    global direction
    if new_direction in ['left', 'right', 'up', 'down']:
        direction = new_direction


def set_key_bindings():
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))


window = Tk()
window.title("Snake game")

canvas_start = Canvas(window, bg='#FF00FF', height=GAME_HEIGHT, width=GAME_WIDTH)
canvas_start.pack()

menu()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

score = 0
highscore = 0
direction = 'down'

set_key_bindings()

window.mainloop()
