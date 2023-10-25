from tkinter import *
import random

root = Tk()
b = Button(root, text = "NYTT SPEL")
s = Button(root, text = "STEN")
x = Button(root, text = "SAX")
p = Button(root, text = "PÅSE")
choice = ""
alternativ = ["sten", "sax", "påse"]

class bot():
    def __init__(self, botchoice):
        self.botchoice = botchoice

bot.botchoice = random.choice(alternativ)

def click_b(self):
    bot.botchoice = random.choice(alternativ)
    lbl["text"] = ""

def click_s(self):
    choice = "sten"
    if choice != bot.botchoice:
        if choice == "sten" and bot.botchoice == "påse":
            vann = "DU FÖRLORADE :("
        elif choice == "sten" and bot.botchoice == "sax":
            vann = "DU VANN :)"
    else:
        vann = "DET BLEV LIKA o_o"
    lbl["text"] = vann

def click_x(self):
    choice = "sax"
    if choice != bot.botchoice:
        if choice == "sax" and bot.botchoice == "påse":
            vann = "DU VANN :)"
        elif choice == "sax" and bot.botchoice == "sten":
            vann = "DU FÖRLORADE :("
    else:
        vann = "DET BLEV LIKA o_o"
    lbl["text"] = vann

def click_p(self):
    choice = "påse"
    if choice != bot.botchoice:
        if choice == "påse" and bot.botchoice == "sten":
            vann = "DU VANN :)"
        elif choice == "påse" and bot.botchoice == "sax":
            vann = "DU FÖRLORADE :("
    else:
        vann = "DET BLEV LIKA o_o"
    lbl["text"] = vann

lbl = Label(root)
lbl.pack()
b.bind("<Button-1>", click_b)
s.bind("<Button-1>", click_s)
x.bind("<Button-1>", click_x)
p.bind("<Button-1>", click_p)
b.pack()
s.pack()
x.pack()
p.pack()

root.mainloop()