import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
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
	"""
	Creates a new Calculator class.
	"""
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid()
		self.init_gui()
		self.master.title("Calculator")
		self.master.resizable(width=False, height=False)
		self.master.bind("key", self.key_binding)
		self.master.bind("<Return>", self.return_key)
		self.mainloop()

	def init_gui(self):
		"""
		Initiates graphical interface (buttons and entry).
		"""
		self.but1 = tk.Button(self, 
		text="1", 
		command=lambda: self.clicked(1),
		**button_param
)
		self.but1.grid(row=1, column=1)
		self.but2 = tk.Button(self, 
		text="2", 
		command=lambda: self.clicked(2),
		**button_param
)
		self.but2.grid(row=1, column=2)
		self.but3 = tk.Button(self, 
		text="3", 
		command=lambda: self.clicked(3),
		**button_param
)
		self.but3.grid(row=1, column=3)
		self.but4 = tk.Button(self, 
		text="4", 
		command=lambda: self.clicked(4),
		**button_param
)
		self.but4.grid(row=2, column=1)
		self.but5 = tk.Button(self, 
		text="5", 
		command=lambda: self.clicked(5),
		**button_param
)
		self.but5.grid(row=2, column=2)
		self.but6 = tk.Button(self, 
		text="6", 
		command=lambda: self.clicked(6),
		**button_param
)
		self.but6.grid(row=2, column=3)
		self.but7 = tk.Button(self, 
		text="7", 
		command=lambda: self.clicked(7),
		**button_param
)
		self.but7.grid(row=3, column=1)
		self.but8 = tk.Button(self, 
		text="8", 
		command=lambda: self.clicked(8),
		**button_param
)
		self.but8.grid(row=3, column=2)
		self.but9 = tk.Button(self, 
		text="9", 
		command=lambda: self.clicked(9),
		**button_param
)
		self.but9.grid(row=3, column=3)
		self.but0 = tk.Button(self, 
		text="0", 
		command=lambda: self.clicked(0),
		**button_param
)
		self.but0.grid(row=4, column=1)
		self.but_C = tk.Button(self, 
		text="C", 
		command=lambda: self.reset(),
		**button_param
)
		self.but_C.grid(row=3, column=6)
		self.but_CE = tk.Button(self, 
		text="CE", 
		command=lambda: self.delete(),
		**button_param
)
		self.but_CE.grid(row=4, column=3)
		self.but_plus = tk.Button(self, 
		text="+", 
		command=lambda: self.clicked("+"),
		**button_param
)
		self.but_plus.grid(row=1, column=4)
		self.but_minus = tk.Button(self, 
		text="-", 
		command=lambda: self.clicked("-"),
		**button_param
)
		self.but_minus.grid(row=2, column=4)
		self.but_mult = tk.Button(self, 
		text="*", 
		command=lambda: self.clicked("*"),
		**button_param
)
		self.but_mult.grid(row=3, column=4)
		self.but_div = tk.Button(self, 
		text="÷", 
		command=lambda: self.clicked("/"),
		**button_param
)
		self.but_div.grid(row=4, column=4)
		self.but_fact = tk.Button(self, 
		text="!", 
		command=lambda: self.factorial(),
		**button_param
)
		self.but_fact.grid(row=2, column=5)
		self.but_pow = tk.Button(self, 
		text="^", 
		command=lambda : self.clicked("**"),
		**button_param
)
		self.but_pow.grid(row=3, column=5)
		self.but_result = tk.Button(self, 
		text="=", 
		command=lambda: self.result(),
		**button_param
)
		self.but_result.grid(row=1, column=5)
		self.but_sqrt = tk.Button(self,
		text="√",
		command=lambda: self.square(),
		**button_param
)		
		self.but_sqrt.grid(row=4, column=5)
		self.but_openparen = tk.Button(self,
		text="(",
		command=lambda: self.clicked("("),
		**button_param
)
		self.but_openparen.grid(row=1, column=6)
		self.but_closeparen = tk.Button(self,
		text=")",
		command=lambda: self.clicked(")"),
		**button_param
)
		self.but_closeparen.grid(row=2, column=6)
		self.but_dot = tk.Button(self,
		text=".",
		command=lambda: self.clicked("."),
		**button_param
)
		self.but_dot.grid(row=4, column=2)
		self.entry = tk.Entry(self, relief="flat", font="Arial 15 bold")
		self.entry.grid(row=0, columnspan=7, sticky=tk.W + tk.E)

	def key_binding(self, event):
		self.entry.insert("end", event.char)

	def clicked(self, char):
		"""
		When button is clicked, the corresponding value is inserted into the entry.
		"""
		self.entry.insert("end", char)

	def reset(self):
		"""
		Resets all the operations passed.
		"""
		self.entry.delete(0, "end")	

	def delete(self):
		"""
		Deletes characters from end of the entry one by one.
		"""
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
		"""
		Calculates the factorial value of the given number.
		"""
		try:
			n = factorial(int(self.entry.get()))
			self.entry.delete(0, "end")
			self.entry.insert("end", n)
		except ValueError:
			tk.messagebox.showwarning(
				title="Invalid Value", 
				message="You entered an invalid value!"
)
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
		"""
		Calculates the result when pressed Enter
		"""
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



def main():
	Calculator()


if __name__ == "__main__":
	main()