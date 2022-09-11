from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
window.title("Py Currency Converter")

first_currency_entry = Entry(width=20)
first_currency_entry.grid(row=0, column=0)

second_currency_label = Label(text="0.00")
second_currency_label.grid(row=1, column=0)

currencies = ["USD", "IRR"]

first_currency_drop_menu_value = StringVar()
first_currency_drop_menu_value.set(currencies[0])
first_currency_drop_menu = OptionMenu(window, first_currency_drop_menu_value, *currencies)
first_currency_drop_menu.config(width=7)
first_currency_drop_menu.grid(row=0, column=1)

second_currency_drop_menu_value = StringVar()
second_currency_drop_menu_value.set(currencies[0])
second_currency_drop_menu = OptionMenu(window, second_currency_drop_menu_value, *currencies)
second_currency_drop_menu.config(width=7)
second_currency_drop_menu.grid(row=1, column=1)

window.mainloop()
