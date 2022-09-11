from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title("Py Currency Converter")

first_currency_entry = Entry(width=20)
first_currency_entry.grid(row=0, column=0)

window.mainloop()
