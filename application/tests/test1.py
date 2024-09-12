import tkinter as tk

win = tk.Tk()

win.geometry(f'400x500+100+200')
win.title('Мое первое приложение')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')

# btn1.pack()
# btn2.pack()

btn1.grid(row=0, column=0)
btn2.grid(row=2, column=1)



win.mainloop()


