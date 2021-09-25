#!/usr/bin/env python3
# -*- config: utf-8 -*-

# виджеты Radiobatton и Checkbutton поддерживают большинство свойств
# оформления внешнего вида, которые есть у других элементов графического интерфейса.
# При этом у Radiobutton есть особое свойство indicatoron . По-умолчанию он равен
# единице, в этом случае радиокнопка выглядит как нормальная радиокнопка. Однако если
# присвоить этой опции ноль, то виджет Radiobutton становится похожим на обычную кнопку
# по внешнему виду. Но не по смыслу.

from tkinter import *


def get_phone():
    v = var.get()
    if v == 0:
        label['text'] = '+7 1234567890'
    elif v == 1:
        label['text'] = '+4 9087654321'
    elif v == 2:
        label['text'] = '+9 1212121212'


root = Tk()

f = Frame()
f.pack(side=LEFT)

var = IntVar()
var.set(-1)
Radiobutton(f, text="Вася", width=10, height=3,
            indicatoron=0, variable=var,
            value=0, command=get_phone).pack()
Radiobutton(f, text="Петя", width=10, height=3,
            indicatoron=0, variable=var,
            value=1, command=get_phone).pack()
Radiobutton(f, text="Маша", width=10, height=3,
            indicatoron=0, variable=var,
            value=2, command=get_phone).pack()

label = Label(bg="white", width=20)
label.pack(side=LEFT, fill=Y)

root.mainloop()
