from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title("Py Currency Converter")

first_currency_entry = Entry(width=20)
first_currency_entry.grid(row=0, column=0)

second_currency_label = Label(text="0.00")
second_currency_label.grid(row=1, column=0)
second_currency_label.config(pady=20)

window.mainloop()
