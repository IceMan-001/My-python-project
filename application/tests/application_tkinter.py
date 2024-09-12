import tkinter as tk

win = tk.Tk()  # создание окна

"""Размеры и геометрия окна"""

photo = tk.PhotoImage(file='../img/satisfaction-icon.png')  # установка значка окна
win.iconphoto(False, photo)

win.config(bg='#FAEBD7')  # установка цвета окна

win.title('Мое графическое приложение')  # изменение подписи окна

win.geometry('500x600+100+200')  # установка размера окна и его отрисовки относительно левого верхнего угла
"""либо так"""
# h = 500
# w = 600
# win.geometry(f'{h}x{w}+100+200')

win.resizable(False, False)  # запрет изменения размера окна пользователем

win.minsize(400, 500)  # минимальный размер окна
win.maxsize(700, 400)  # максимальный размер окна

"""Виджет Label"""
ladle_1 = tk.Label(win, text='Hello',
                   bg='red',
                   fg='white',
                   font=('Arial', 15, 'bold'),
                   # padx=10,
                   # pady=20
                   width=10,
                   height=5,
                   relief=tk.RAISED,
                   bd=10)  # Первый параметр где разместить и какую надпись отобразить
ladle_1.pack()

"""Виджет Button"""


def say_hello():
    print('hello!')


def add_label():
    label = tk.Label(win, text='new')
    label.pack()


btn1 = tk.Button(win, text='Hello', command=say_hello)
btn1.pack()

btn2 = tk.Button(win, text='Add new label', command=add_label)
btn2.pack()

win.mainloop()  # отрисовка окна
