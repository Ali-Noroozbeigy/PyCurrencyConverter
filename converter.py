from tkinter import *
import requests
from tkinter import messagebox


def fetch_available_currencies():
    headers = {
        "apikey": "0yzKYae0fkOEb8p5L3Yu1itjDHursb0L"
    }

    response = requests.get(url="https://api.apilayer.com/currency_data/list", headers=headers)
    response.raise_for_status()

    currencies_dictionary = {}

    # swapping short form and long form
    for short_form, long_form in response.json()["currencies"].items():
        currencies_dictionary[long_form] = short_form

    return currencies_dictionary


def convert():
    try:
        amount = float(first_currency_entry.get())
    except ValueError:
        messagebox.showerror("Error!", "Please enter number in the field")
    else:
        first_currency = available_currencies[first_currency_drop_menu_value.get()]  # to get short form
        second_currency = available_currencies[second_currency_drop_menu_value.get()]

        headers = {
            "apikey": "0yzKYae0fkOEb8p5L3Yu1itjDHursb0L"
        }

        params = {
            "to": second_currency,
            "from": first_currency,
            "amount": amount
        }

        response = requests.get(url="https://api.apilayer.com/currency_data/convert", params=params, headers=headers)
        response.raise_for_status()

        result = response.json()["result"]

        second_currency_label.config(text=str(result))


window = Tk()
window.config(padx=50, pady=50)
window.title("Py Currency Converter")

first_currency_entry = Entry(width=20)
first_currency_entry.focus()
first_currency_entry.grid(row=0, column=0, padx=20, pady=20)

second_currency_label = Label(text="0.00")
second_currency_label.grid(row=1, column=0, padx=20, pady=20)

available_currencies = fetch_available_currencies()
currencies = list(available_currencies.keys())

first_currency_drop_menu_value = StringVar()
first_currency_drop_menu_value.set(currencies[0])
first_currency_drop_menu = OptionMenu(window, first_currency_drop_menu_value, *currencies)
first_currency_drop_menu.config(width=50)
first_currency_drop_menu.grid(row=0, column=1, padx=20, pady=20)

second_currency_drop_menu_value = StringVar()
second_currency_drop_menu_value.set(currencies[1])
second_currency_drop_menu = OptionMenu(window, second_currency_drop_menu_value, *currencies)
second_currency_drop_menu.config(width=50)
second_currency_drop_menu.grid(row=1, column=1, padx=20, pady=20)

submit_button = Button(text="Convert", command=convert)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

window.mainloop()
