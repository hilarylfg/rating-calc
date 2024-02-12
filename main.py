from customtkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def open_calc():
    global radiovar, e1, e2, e3, e4, label
    calc_rating = CTkToplevel(root)
    calc_rating.title('Средний балл атестатта')
    calc_rating.geometry('350x250')
    calc_rating.configure(background='white')

    label = CTkLabel(master=calc_rating, text='', font=("Avenir", 25), justify=CENTER)
    label.pack(pady=12)

    btn = CTkButton(master=calc_rating, text="Вычислить средний балл", command=calc,
    fg_color='#2A2F4F', hover_color='#5F4A87', corner_radius=12)
    btn.place(x=90, y=50)

    label1 = CTkLabel(master=calc_rating, text='Кол-во пятёрок →', font=("Avenir", 15))
    label1.place(x=84, y=90)
    e1 = CTkEntry(master=calc_rating, width=50, justify=CENTER, corner_radius=12)
    e1.insert(0, "0")
    e1.place(x=220, y=90)

    label2 = CTkLabel(master=calc_rating, text='Кол-во четвёрок →', font=("Avenir", 15))
    label2.place(x=75, y=130)
    e2 = CTkEntry(master=calc_rating, width=50, justify=CENTER, corner_radius=12)
    e2.insert(0, "0")
    e2.place(x=220, y=130)

    label3 = CTkLabel(master=calc_rating, text='Кол-во троек →', font=("Avenir", 15))
    label3.place(x=100, y=170)
    e3 = CTkEntry(master=calc_rating, width=50, justify=CENTER, corner_radius=12)
    e3.insert(0, "0")
    e3.place(x=220, y=170)

    label4 = CTkLabel(master=calc_rating, text='Кол-во двоек →', font=("Avenir", 15))
    label4.place(x=100, y=210)
    e4 = CTkEntry(master=calc_rating, width=50, justify=CENTER, corner_radius=12)
    e4.insert(0, "0")
    e4.place(x=220, y=210)

    radiovar = IntVar(value=2)

    R1 = CTkRadioButton(calc_rating, text='1', variable=radiovar, value=1, width=5, height=5,
    radiobutton_width=10, radiobutton_height=10, fg_color='#5F4A87', hover_color='#2A2F4F')
    R1.place(x=2, y=57)

    R2 = CTkRadioButton(calc_rating, text='2', variable=radiovar, value=2, width=5, height=5,
    radiobutton_width=10, radiobutton_height=10, fg_color='#5F4A87', hover_color='#2A2F4F')
    R2.place(x=32, y=57)

    R3 = CTkRadioButton(calc_rating, text='3', variable=radiovar, value=3, width=5, height=5,
    radiobutton_width=10, radiobutton_height=10, fg_color='#5F4A87', hover_color='#2A2F4F')
    R3.place(x=62, y=57)

    calc_rating.mainloop()
def calc():
    try:
        entry5 = int(e1.get())
        entry4 = int(e2.get())
        entry3 = int(e3.get())
        entry2 = int(e4.get())
        count = entry5 + entry4 + entry3 + entry2
        summa = (entry5 * 5) + (entry4 * 4) + (entry3 * 3) + (entry2 * 2)
        main = summa / count
        dot = radiovar.get()
        main = round(main, dot)
        label.configure(text=main)
        if main <= 5 and main > 4.69:
            label.configure(text_color="Green")
        if main <= 4.69 and main > 3.69:
            label.configure(text_color="Green")
        if main <= 3.69 and main > 2.69:
            label.configure(text_color="Orange")
        if main <= 2.69:
            label.configure(text_color="Red")
    except ZeroDivisionError:
        label.configure(text='Вы не ввели свои оценки!', text_color="Red")
    except ValueError:
        label.configure(text='Числа некорректные!', text_color="Red")

def open_graph():
    global entry_graph, calc_graph
    calc_graph = CTkToplevel(root)
    calc_graph.title("Калькулятор с графиком")

    label_graph = CTkLabel(calc_graph, text="Введите функцию y(x): ", font=("Avenir", 18), justify=CENTER)
    label_graph.pack()

    entry_graph = CTkEntry(calc_graph)
    entry_graph.pack()

    button_graph = CTkButton(master=calc_graph, text="Построить график", command=graph,
    fg_color='#2A2F4F', hover_color='#5F4A87', corner_radius=12)
    button_graph.pack()
def graph():
    try:
        xy = entry_graph.get()
        x = np.linspace(-10, 10, 400)
        y = eval(xy)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('График функции')

        canvas = FigureCanvasTkAgg(fig, master=calc_graph)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except Exception as e:
        messagebox.showerror("Ошибка", "Некорректное выражение")

root = CTk()
root.title('Калькуляторы')
root.geometry('350x200')

label_root = CTkLabel(master=root, text='Выберите калькулятор', font=("Avenir", 25), justify=CENTER)
label_root.place(x=45, y=10)

button_root1 = CTkButton(master=root, text="Калькулятор оценок", command=open_calc,
fg_color='#2A2F4F', hover_color='#5F4A87', corner_radius=12)
button_root1.place(x=100, y=60)

button_root2 = CTkButton(master=root, text="Графический калькулятор", command=open_graph,
fg_color='#2A2F4F', hover_color='#5F4A87', corner_radius=12)
button_root2.place(x=80, y=100)

root.mainloop()