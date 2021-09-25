#!/usr/bin/env python3
# -*- config: utf-8 -*-

# перепишите программу из пункта 8 так, чтобы интерфейс выглядел
# примерно следующим образом:

from tkinter import *


class Window(Tk):
    # создание окна
    def __init__(self):
        super().__init__()
        self.title('Радуга')
        self.geometry("280x220")  # размер окна
        # окно, в котором прописывается текст и обозначение
        self.lbl = Label(text="Радуга", width=280)
        self.e1 = Entry(width=280, justify=CENTER)
        self.lbl.pack()
        self.e1.pack()
        # обозначения и названия цветов
        dct = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый', }
        buttons = Frame(self)
        buttons.pack()
        for colour in dct.keys():
            func = lambda c=colour, ruc=dct[colour]: self.onclick(c, ruc)
            b = Button(buttons, text='', command=func, bg=colour, width=1, height=1, )  # кнопки
            b.pack(side=RIGHT)

    # очистка строчки при новом нажатии на цвет и появление нового
    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour


# закрытие окна
if __name__ == '__main__':
    root = Window()
    root.mainloop()
