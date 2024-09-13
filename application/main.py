from tkinter import *
import tkinter as tk
from PIL import ImageTk


def get_entry_rectangle():
    try:
        value1 = int(pole1.get())
        value2 = int(pole2.get())
        answer.configure(
            text=f'Площадь квадрата при введенных \n значениях {value1} и {value2} \nравна: {value1 * value2}',
            fg='black')
        pole1.delete(0, END)
        pole2.delete(0, END)
    except ValueError:
        answer.configure(text='Введите корректные данные!', fg='red')
        pole1.delete(0, END)
        pole2.delete(0, END)


def get_entry_circle():
    try:
        value3 = int(pole3.get())
        answer.configure(text=f'Площадь круга при введенном \n радиусе {value3}\n равна: {3.14 * value3 * value3}',
                         fg='black')
        pole3.delete(0, END)
    except ValueError:
        answer.configure(text='Введите корректные данные!', fg='red')
        pole3.delete(0, END)


win = tk.Tk()

photo = tk.PhotoImage(file='img/satisfaction-icon.png')  # установка значка окна
win.iconphoto(False, photo)

color = '#FAEBD7'
win.config(bg=color)  # установка цвета окна

win.title('Мое графическое приложение')  # изменение подписи окна

h = 500
w = 600
win.geometry(f'{h}x{w}+100+200')

win.resizable(False, False)

label = tk.Label(win, text='Вычислить площадь прямоугольника', font=('Arial', 10, 'bold'), bg=color)
label.place(relx=0.96, rely=0.03, anchor='e')
image = ImageTk.PhotoImage(file="img/1square_PNG41.png")
btn = tk.Button(win, relief=tk.RAISED, bd=5, width=200, height=100, image=image, command=get_entry_rectangle)
btn.place(relx=0.5, rely=0.15, anchor='w')

n = tk.Label(win, text='Введите данные', bg='#FAEBD7')
n.place(relx=0.28, rely=0.07, anchor='e')
n1 = tk.Label(win, text='Введите данные', bg='#FAEBD7')
n1.place(relx=0.28, rely=0.35, anchor='e')

pole1 = tk.Entry(win)
pole1.place(x=30, y=60)
pole2 = tk.Entry(win)
pole2.place(x=30, y=80)
pole3 = tk.Entry(win)
pole3.place(x=30, y=230)

label1 = tk.Label(win, text='Вычислить площадь круга', font=('Arial', 10, 'bold'), bg=color)
label1.place(relx=0.9, rely=0.3, anchor='e')
image1 = ImageTk.PhotoImage(file="img/1df5e39de81f2076e3b6ec32af96cdeb2.png")
btn1 = tk.Button(win, relief=tk.RAISED, bd=5, width=200, height=100, image=image1, command=get_entry_circle)
btn1.place(relx=0.5, rely=0.42, anchor='w')

answer = tk.Label(win, text='Вывод результата вычисления...', font=('Arial', 12, 'bold'), bg=color)
answer.place(x=150, y=425)

win.mainloop()
