from tkinter import *
import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='guestbook'
)


def run(x,y):
    mycursor = mydb.cursor()

    sql = "INSERT INTO comments (name, comment) VALUES (%s, %s)"
    val = (x, y)
    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.execute("select * from comments")

    myresult = mycursor.fetchall()

    for i in myresult:
        print(i)


window = Tk()
window.title("Snake game")

canvas_start = Canvas(window, bg='#000000', height=500, width=500)
canvas_start.pack()

window.resizable(False, False)

entry1 = tk.Entry(window,textvariable = '', font=('calibre',10,'normal'))

entry2 = tk.Entry(window,textvariable = '', font=('calibre',10,'normal'))

entry1.grid(row=0,column=0)
entry2.grid(row=1,column=0)

window.mainloop()

button = Button(window, text='FOOD COLOR', height='5', width='20', command=run(entry1, entry2))
button.place(x=260, y=400)

