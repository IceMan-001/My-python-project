from tkinter import *
import tkinter as tk
from PIL import ImageTk


def body_mass_index():
    try:
        the_height = float(pole1.get())
        the_weight = float(pole2.get())

        bmi = the_weight / (the_height / 100) ** 2

        the_bmi = round(bmi, 1)

        const_text = \
            f'При введенном росте {the_height} см. и весе {the_weight} кг.\nиндекс массы тела составляет {the_bmi}'

        if the_bmi <= 18.5:
            answer.configure(
                text=f'Упс! У вас недостаточный вес.\n{const_text}\n\N{unamused face}\N{unamused face}\N{unamused face}',
                fg='#FF4500')
            answer.place(x=70, y=425)

        elif the_bmi <= 24.9:
            answer.configure(
                text=f'Классно! Вы здоровы.\n{const_text}\n'
                     f'\N{smiling face with sunglasses}\N{smiling face with sunglasses}\N{smiling face with sunglasses}',
                fg='#006400')
            answer.place(x=70, y=425)

        elif the_bmi <= 29.9:
            answer.configure(
                text=f'Ииии! У тебя избыточный вес.\n{const_text}\n'
                     f'\N{zipper-mouth face}\N{zipper-mouth face}\N{zipper-mouth face}',
                fg='#FF0000')
            answer.place(x=70, y=425)

        else:
            answer.configure(
                text=f'Блин! У тебя ожирение.\n{const_text}\n\N{angry face}\N{angry face}\N{angry face}',
                fg='#8B0000')
            answer.place(x=70, y=425)

        pole1.delete(0, END)
        pole2.delete(0, END)
    except ValueError:
        answer.configure(text='Введите корректные данные!', fg='red')
        answer.place(x=135, y=425)
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
win.geometry(f'{h}x{w}+600+200')

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
answer.place(x=123, y=425)

win.resizable(False, False)

win.mainloop()
