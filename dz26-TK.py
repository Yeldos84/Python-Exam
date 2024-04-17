import tkinter
from tkinter import ttk

from tkinter import *


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        # self.title('Tkinter')
        # self.geometry('500x500')
        ttk.Style().theme_use("clam")
        self.btn_style = ttk.Style()
        self.btn_style.configure("My.TButton", foreground="#fff", background="#ff5252")
        self.btn_style.configure("Y.TButton", foreground="#fff", background="#e5a536")

        # frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
        # frame.place(relx=0.55, rely=0.2, anchor='c', width=300, height=30)

        self.inp = ttk.Entry(font=("Arial", 14))
        self.inp.focus_set()
        self.inp.place(relx=0.50, rely=0.1, anchor="c", width=300, height=30)

        self.label = Label(
            relief="sunken",
            background="#FFCDD2",
            font=("Arial", 14),
            foreground="#B71C1C",
        )
        self.label.place(relx=0.50, rely=0.2, anchor="c", width=300, height=30)

        self.btn = ttk.Button(text="7", command=lambda t=7: self.clicked(t))
        self.btn.place(relx=0.20, rely=0.3, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="8", command=lambda t=8: self.clicked(t))
        self.btn.place(relx=0.40, rely=0.3, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="9", command=lambda t=9: self.clicked(t))
        self.btn.place(relx=0.60, rely=0.3, anchor="c", width=50, height=40)
        self.btn = ttk.Button(
            text="/", style="Y.TButton", command=lambda t="/": self.clicked(t)
        )
        self.btn.place(relx=0.80, rely=0.3, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="4", command=lambda t=4: self.clicked(t))
        self.btn.place(relx=0.20, rely=0.5, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="5", command=lambda t=5: self.clicked(t))
        self.btn.place(relx=0.40, rely=0.5, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="6", command=lambda t=6: self.clicked(t))
        self.btn.place(relx=0.60, rely=0.5, anchor="c", width=50, height=40)
        self.btn = ttk.Button(
            text="*", style="Y.TButton", command=lambda t="*": self.clicked(t)
        )
        self.btn.place(relx=0.80, rely=0.5, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="1", command=lambda t=1: self.clicked(t))
        self.btn.place(relx=0.20, rely=0.7, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="2", command=lambda t=2: self.clicked(t))
        self.btn.place(relx=0.40, rely=0.7, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="3", command=lambda t=3: self.clicked(t))
        self.btn.place(relx=0.60, rely=0.7, anchor="c", width=50, height=40)
        self.btn = ttk.Button(
            text="-", style="Y.TButton", command=lambda t="-": self.clicked(t)
        )
        self.btn.place(relx=0.80, rely=0.7, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="C", command=self.clear)
        self.btn.place(relx=0.20, rely=0.9, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="0", command=lambda t=0: self.clicked(t))
        self.btn.place(relx=0.40, rely=0.9, anchor="c", width=50, height=40)
        self.btn = ttk.Button(text="=", style="My.TButton", command=self.equal)
        self.btn.place(relx=0.60, rely=0.9, anchor="c", width=50, height=40)
        self.btn = ttk.Button(
            text="+", style="Y.TButton", command=lambda t="+": self.clicked(t)
        )
        self.btn.place(relx=0.80, rely=0.9, anchor="c", width=50, height=40)

    def clicked(self, t):
        self.inp.insert(END, t)

    def equal(self):
        try:
            self.label["text"] = f"{eval(self.inp.get()):.2f}".rstrip("0").rstrip(".")
            self.inp.delete(0, last=END)
            self.inp.insert(0, str(self.label["text"]))
        except ZeroDivisionError:
            self.inp.delete(0, last=END)
            self.inp.insert(0, "Деление на ноль невозможно!")

    def clear(self):
        self.inp.delete(0, last=END)
        self.label["text"] = ""

    def new_window(self):
        self.new_win = MainWindow()
        self.new_win.title("Валюта")
        self.new_win.geometry("250x250")
        self.valuta = ["KZT", "USA"]
        combobox = ttk.Combobox(self.new_win, values=self.valuta)
        combobox.pack(anchor=CENTER, padx=6, pady=6)
        valuta_label = ttk.Label(self.new_win, text="<-->")
        valuta_label.pack(anchor=CENTER, padx=6, pady=6)
        combobox2 = ttk.Combobox(self.new_win, values=self.valuta)
        combobox2.pack(anchor=CENTER, padx=6, pady=6)
        valuta_entry = ttk.Entry(self.new_win)
        valuta_entry.pack(anchor=CENTER, padx=10, pady=10)


# root = Tk()
# root.title('dsfsd')
# root.geometry('500x500')
window = MainWindow()
window.title("Калькулятор")
window.geometry("400x400")
window.resizable(False, False)
main_menu = Menu()
file_menu = Menu(tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Валюта", command=window.new_window)
file_menu.add_command(label="Объем")
file_menu.add_command(label="Закрыть", command=lambda: window.destroy())
window.config(menu=main_menu)
window.mainloop()
