import tkinter as tk
from tkinter import messagebox
import parser
from math import sqrt, factorial


button_param = {
    "relief": "flat",
    "height": 3,
    "width": 3,
    "font": "Courier 11 bold",
    "activebackground": "gray74"
}


class Calculator(tk.Frame):
    def __init__(self, master=None):
        """Create a frame widget with the parent MASTER for the class Calculator."""
        tk.Frame.__init__(self, master)
        self.grid()
        self.master.title("Calculator")
        self.master.resizable(width=False, height=False)
        self.but1 = tk.Button(
            self, text="1", command=lambda arg=1: self.clicked(arg), **button_param)
        self.but1.grid(row=1, column=1)
        self.but2 = tk.Button(
            self, text="2", command=lambda arg=2: self.clicked(arg), **button_param)
        self.but2.grid(row=1, column=2)
        self.but3 = tk.Button(
            self, text="3", command=lambda arg=3: self.clicked(arg), **button_param)
        self.but3.grid(row=1, column=3)
        self.but4 = tk.Button(
            self, text="4", command=lambda arg=4: self.clicked(arg), **button_param)
        self.but4.grid(row=2, column=1)
        self.but5 = tk.Button(
            self, text="5", command=lambda arg=5: self.clicked(arg), **button_param)
        self.but5.grid(row=2, column=2)
        self.but6 = tk.Button(
            self, text="6", command=lambda arg=6: self.clicked(arg), **button_param)
        self.but6.grid(row=2, column=3)
        self.but7 = tk.Button(
            self, text="7", command=lambda arg=7: self.clicked(arg), **button_param)
        self.but7.grid(row=3, column=1)
        self.but8 = tk.Button(
            self, text="8", command=lambda arg=8: self.clicked(arg), **button_param)
        self.but8.grid(row=3, column=2)
        self.but9 = tk.Button(
            self, text="9", command=lambda arg=9: self.clicked(arg), **button_param)
        self.but9.grid(row=3, column=3)
        self.but0 = tk.Button(
            self, text="0", command=lambda arg=0: self.clicked(arg), **button_param)
        self.but0.grid(row=4, column=1)
        self.but_C = tk.Button(
            self, text="C", command=self.reset, **button_param)
        self.but_C.grid(row=3, column=6)
        self.but_CE = tk.Button(
            self, text="CE", command=self.delete, **button_param)
        self.but_CE.grid(row=4, column=3)
        self.but_plus = tk.Button(
            self, text="+", command=lambda arg="+": self.clicked(arg), **button_param)
        self.but_plus.grid(row=1, column=4)
        self.but_minus = tk.Button(
            self, text="-", command=lambda arg="-": self.clicked(arg), **button_param)
        self.but_minus.grid(row=2, column=4)
        self.but_multi = tk.Button(
            self, text="*", command=lambda arg="*": self.clicked(arg), **button_param)
        self.but_multi.grid(row=3, column=4)
        self.but_div = tk.Button(
            self, text="÷", command=lambda arg="/": self.clicked(arg), **button_param)
        self.but_div.grid(row=4, column=4)
        self.but_fact = tk.Button(
            self, text="!", command=self.factorial, **button_param)
        self.but_fact.grid(row=2, column=5)
        self.but_pow = tk.Button(
            self, text="^", command=lambda arg="**": self.clicked(arg), **button_param)
        self.but_pow.grid(row=3, column=5)
        self.but_result = tk.Button(
            self, text="=", command=self.result, **button_param)
        self.but_result.grid(row=1, column=5)
        self.but_square_root = tk.Button(
            self, text="√", command=self.square, **button_param)
        self.but_square_root.grid(row=4, column=5)
        self.but_open_paren = tk.Button(
            self, text="(", command=lambda arg="(": self.clicked(arg), **button_param)
        self.but_open_paren.grid(row=1, column=6)
        self.but_close_paren = tk.Button(
            self, text=")", command=lambda arg=")": self.clicked(arg), **button_param)
        self.but_close_paren.grid(row=2, column=6)
        self.but_dot = tk.Button(
            self, text=".", command=lambda arg=".": self.clicked(arg), **button_param)
        self.but_dot.grid(row=4, column=2)
        self.entry = tk.Entry(self, relief="flat", font="Arial 15 bold")
        self.entry.grid(row=0, columnspan=7, sticky=tk.W + tk.E)
        self.master.bind("key", self.key_binding)
        self.master.bind("<Return>", self.return_key)
        self.mainloop()

    def key_binding(self, event):
        self.entry.insert("end", event.char)

    def clicked(self, char):
        """When button is clicked, the corresponding value is inserted into the entry."""
        self.entry.insert("end", char)

    def reset(self):
        """Reset all the operations passed."""
        self.entry.delete(0, "end")

    def delete(self):
        """Delete characters from end of the entry one by one."""
        entry = self.entry.get()
        self.reset()
        entry_new = entry[:-1]
        self.entry.insert(0, entry_new)

    def result(self):
        try:
            result = eval(parser.expr(self.entry.get()).compile())
            self.entry.delete(0, "end")
            self.entry.insert("end", result)
        except ZeroDivisionError:
            tk.messagebox.showerror(
                title="Zero Division",
                message="Cannot be divided by zero!"
            )
            self.entry.delete(0, "end")
        except SyntaxError:
            tk.messagebox.showerror(
                title="Invalid Operation",
                message="Invalid operation!"
            )
            self.entry.delete(0, "end")

    def factorial(self):
        """Calculate the factorial value of the given number."""
        try:
            n = factorial(int(self.entry.get()))
            self.entry.delete(0, "end")
            self.entry.insert("end", n)
        except ValueError:
            tk.messagebox.showerror(
                title="Invalid Value",
                message="You entered an invalid value!")
            self.entry.delete(0, "end")
        except OverflowError:
            tk.messagebox.showerror(
                title="Overflow",
                message="Value exceeded the limit!")
            self.entry.delete(0, "end")

    def square(self):
        try:
            result = sqrt(int(self.entry.get()))
            self.entry.delete(0, "end")
            self.entry.insert("end", result)
        except ValueError:
            tk.messagebox.showerror(
                title="Invalid Value",
                message="You entered an invalid value!"
            )
            self.entry.delete(0, "end")

    def return_key(self, event):
        """Calculate the result when pressed Enter."""
        self.result()


def main():
    Calculator()


if __name__ == "__main__":
    main()
