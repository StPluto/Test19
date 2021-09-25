#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу, состоящую из однострочного и многострочного
# текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
# открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
# должно загружаться в поле типа Text .

from tkinter import *


def load():
    ent.get()
    with open('text.txt', 'r') as f:
        result = text.insert(0.1, f.read())
        return result


def save():
    form = text.get(0.1, 'end')
    ent.get()
    with open('text.txt', 'r+') as f:
        f.write(form)


root = Tk()
f_top = Frame(root)
f_bot = Frame(root)
ent = Entry(f_top, width=20)
but1 = Button(
    f_top,
    width=10,
    text="Открыть"
)
but2 = Button(
    f_top,
    width=10,
    text="Сохранить"
)
text = Text(f_bot, width=40, height=20)

but1.config(command=load)
but2.config(command=save)

f_top.pack()
f_bot.pack()
ent.pack(side=LEFT, padx=10)
but1.pack(side=LEFT, padx=5)
but2.pack(side=LEFT)
text.pack(side=LEFT)

root.mainloop()
