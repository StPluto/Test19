#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу, состоящую из семи кнопок, цвета которых
# соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
# вставляться код цвета, а в метку – название цвета.

from tkinter import *


class Frame(Tk):

    # создание окна
    def __init__(self):
        super().__init__()
        self.title('Радуга')
        self.geometry("280x220")  # размер окна

        self.lbl = Label(text="Радуга", width=280)
        self.e1 = Entry(width=280, justify=CENTER)
        # обозначения и названия цветов
        dct = {'#ff0000': 'Красный',
               '#ff7d00': 'Оранжевый',
               '#ffff00': 'Желтый',
               '#00ff00': 'Зеленый',
               '#007dff': 'Голубой',
               '#0000ff': 'Синий',
               '#7d00ff': 'Фиолетовый', }
        # окно, в котором прописывается текст и обозначение
        for colour in dct.keys():
            func = lambda c=colour, ruc=dct[colour]: self.onclick(c, ruc)
            b = Button(text='', command=func, bg=colour, width=40, height=1, )  # кнопки
            self.lbl.pack()
            self.e1.pack()
            b.pack()

    # очистка строчки при новом нажатии на цвет и появление нового
    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour


# закрытие окна
if __name__ == '__main__':
    root = Frame()
    root.mainloop()
