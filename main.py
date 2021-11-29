from tkinter import ttk
from tkinter import *
import requests
from bs4 import BeautifulSoup
import dane


def search_with_selenium():
    pass


def search_with_soup():
    pass


def search(options, word):
    print(word)
    print(options)


# GUI Interface
def app():
    window = Tk()
    window.config(padx=25, pady=15, bg="#F0F8FF")
    window.title("Bible Dictionary")

    def check():
        return [dane.dict_list[available_options.index(option)] for option in available_options if option.get() == 1]

    available_options = [IntVar() for _ in range(len(dane.dict_list))]

    style = ttk.Style()
    style.configure("TButton", background="#F0F8FF", font=("Arial", 8, "normal"))
    style.configure("TCheckbutton", background="#F0F8FF", font=("Arial", 8, "italic"))
    style.configure("TEntry", background="#F0F8FF")
    style.configure("TLabel", background="#F0F8FF", font=("Arial", 7, "italic"))

    search_field = ttk.Entry(window, style="TEntry")
    search_button = ttk.Button(window, text="Search", style="TButton", command=lambda: search(check(), search_field.get()))

    search_field.grid(row=0, column=0, padx=5)
    search_button.grid(row=1, column=0, pady=10, rowspan=2)

    num = 0
    current_column = 1
    current_row = 0
    for dict_name in dane.dict_list:
        new_label = ttk.Checkbutton(window, text=dict_name.split(",")[0], style="TCheckbutton", variable=available_options[num])
        if num % 14 == 0:
            current_row = 0
            current_column += 1
        else:
            current_row += 1
        new_label.grid(row=current_row, column=current_column, padx=5, sticky=EW)
        num += 1

    window.mainloop()


app()
