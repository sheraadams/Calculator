from tkinter import *
# defined colors
neon = "#C55FFC"
lpurple = "#EFDCF9"
dark = "#323E42"
dpurple = "#7954A1"
back = "#278ED5"
blue = "#66b6d2"
purple = "#65FC6A"
green = "#96be25"
expression = ""


def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	gui = Tk()
	gui.configure(background= neon, padx=20, pady=20)

	gui.title("Calculator")
	gui.geometry("445x480")

	equation= StringVar()
	expression_field = Entry(gui, textvariable=equation, font='Calibri 20 bold')
	expression_field.grid(columnspan=4, ipadx=60, ipady=10)

	s4 = Label(gui, bg=neon, fg=neon,)
	s4.grid()
	button1 = Button(gui, text=' 1 ', fg=neon, bg=purple,
					command=lambda: press(1), height=2, width=8,  font='Calibri 16 bold')
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg=neon, bg=purple,
					command=lambda: press(2), height=2, width=8,   font='Calibri 16 bold')
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg=neon, bg=purple,
					command=lambda: press(3), height=2, width=8,  font='Calibri 16 bold')
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg=neon, bg=purple,
					command=lambda: press(4), height=2, width=8, font='Calibri 16 bold')
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg=neon, bg=purple,
					command=lambda: press(5), height=2, width=8,  font='Calibri 16 bold')
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg=neon, bg=purple,
					command=lambda: press(6), height=2, width=8,  font='Calibri 16 bold')
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg=neon, bg=purple,
					command=lambda: press(7), height=2, width=8,  font='Calibri 16 bold')
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg=neon, bg=purple,
					command=lambda: press(8), height=2, width=8,  font='Calibri 16 bold')
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg=neon, bg=purple,
					command=lambda: press(9), height=2, width=8, font='Calibri 16 bold')
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg=neon, bg=purple,
					command=lambda: press(0), height=2, width=8, font='Calibri 16 bold')
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg=neon, bg=purple,
				command=lambda: press("+"), height=2, width=8,  font='Calibri 16 bold')
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg=neon, bg=purple,
				command=lambda: press("-"), height=2, width=8, font='Calibri 16 bold')
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg=neon, bg=purple,
					command=lambda: press("*"), height=2, width=8, font='Calibri 16 bold')
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg=neon, bg=purple,
					command=lambda: press("/"), height=2, width=8, font='Calibri 16 bold')
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg=neon, bg=purple,
				command=equalpress, height=2, width=8, font='Calibri 16 bold')
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg=neon, bg=purple,
				command=clear, height=2, width=8, font='Calibri 16 bold')
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg=neon, bg=purple,
					command=lambda: press('.'), height=2, width=8, font='Calibri 16 bold')
	Decimal.grid(row=6, column=0)


	# start the GUI main loop
	gui.mainloop()