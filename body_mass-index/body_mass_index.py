from tkinter import *
import tkinter as tk
from PIL import ImageTk


def body_mass_index():
    try:
        the_height = int(pole1.get())
        the_weight = int(pole2.get())

        the_bmi = the_weight / (the_height / 100) ** 2

        if the_bmi <= 18.5:
            answer.configure(
                text=f'Oops! You are underweight.\nросте{the_height} и весе {the_weight} \nиндекс{the_bmi}\n'
                     f'\N{unamused face}\N{unamused face}\N{unamused face}', fg='black')

        elif the_bmi <= 24.9:
            answer.configure(
                text=f'Awesome! You are healthy.\nросте{the_height} и весе {the_weight} \nиндекс{the_bmi}\n',
                fg='black')

        elif the_bmi <= 29.9:
            answer.configure(
                text=f'Eee! You are overweight.\nросте{the_height} и весе {the_weight} \nиндекс{the_bmi}',
                fg='black')

        else:
            answer.configure(
                text=f'Seesh! You are obese.\nросте{the_height} и весе {the_weight} \nиндекс{the_bmi}',
                fg='black')

        pole1.delete(0, END)
        pole2.delete(0, END)
    except ValueError:
        answer.configure(text='Введите корректные данные!', fg='red')
        pole1.delete(0, END)
        pole2.delete(0, END)


win = tk.Tk()

photo = tk.PhotoImage(file='img/satisfaction-icon.png')  # установка значка окна
win.iconphoto(False, photo)

color = '#FAEBD7'
win.config(bg=color)  # установка цвета окна

win.title('Расчет индекса массы тела')  # изменение подписи окна

h = 500
w = 600
win.geometry(f'{h}x{w}+100+200')

label = tk.Label(win, text='Вычислить массу тела', font=('Arial', 10, 'bold'), bg=color)
label.place(relx=0.68, rely=0.37, anchor='e')
image = ImageTk.PhotoImage(file="img/satisfaction-icon_1.png")
btn = tk.Button(win, relief=tk.RAISED, bd=5, width=200, height=100, image=image, command=body_mass_index)
btn.place(relx=0.3, rely=0.5, anchor='w')

n = tk.Label(win, text='Введите рост', bg='#FAEBD7')
n.place(relx=0.60, rely=0.07, anchor='e')
n1 = tk.Label(win, text='Введите вес', bg='#FAEBD7')
n1.place(relx=0.59, rely=0.2, anchor='e')

pole1 = tk.Entry(win)
pole1.place(x=200, y=60)
pole2 = tk.Entry(win)
pole2.place(x=200, y=140)

answer = tk.Label(win, text='Вывод результата вычисления...', font=('Arial', 12, 'bold'), bg=color)
answer.place(x=150, y=425)

win.resizable(False, False)

win.mainloop()
