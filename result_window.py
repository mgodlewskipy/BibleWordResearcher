from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk


class NewAppWindow:
    def __init__(self):
        self.window = Tk()
        self.window.eval('tk::PlaceWindow . center')
        self.window.config(padx=25, pady=15, bg="#F0F8FF")
        self.window.title("Bible Dictionary")

        self.style = ttk.Style()
        self.style.configure("TButton", background="#F0F8FF", font=("Arial", 8, "normal"))
        self.style.configure("TCheckbutton", background="#F0F8FF", font=("Arial", 8, "italic"))
        self.style.configure("TEntry", background="#F0F8FF")
        self.style.configure("TLabel", background="#F0F8FF", font=("Arial", 7, "italic"))

        self.search_field = ttk.Entry(self.window, style="TEntry")
        self.search_button = ttk.Button(self.window, text="Search", style="TButton")
        self.search_button.invoke()

        self.search_field.grid(row=0, column=0, padx=5)
        self.search_button.grid(row=1, column=0, pady=10, rowspan=2)

        self.setfocus()
        self.window.bind('<Return>', lambda event=None: self.search_button.invoke())

        self.checkbutton_status = []
        self.current_page = 0

    def empty_entry_warning(self):
        def exit_window():
            warning_window.destroy()
            self.window.deiconify()

        self.window.withdraw()
        warning_window = Tk()
        warning_window.title("Bible Dictionary")
        warning_window.eval(f'tk::PlaceWindow {str(warning_window)} center')
        warning_window.config(padx=25, pady=15, bg="#F0F8FF")

        warning_label = Label(warning_window, bg="#F0F8FF", font=("Arial", 8, "normal"), text="Nic nie zostało wpisane w polu wyszukiwania\nlub nie została wybrana żadna opcja")
        warning_label.grid(column=0, row=0)

        warning_button = ttk.Button(warning_window, text="Ok", style="TButton", command=exit_window)
        warning_button.grid(column=0, row=1, pady=10)

    def setfocus(self):
        self.search_field.focus_set()

    def add_options(self, names):
        self.checkbutton_status = [IntVar() for _ in range(len(names))]
        currentrow = 0
        for name in names:
            new_option = ttk.Checkbutton(self.window, text=name, style="TCheckbutton", variable=self.checkbutton_status[names.index(name)], command=self.setfocus)
            new_option.grid(column=1, row=currentrow, sticky=EW)
            currentrow += 1
    
    def result_self_window(self, text, translated):
        def refresh():
            pass

        def next_page():
            if not self.current_page + 1 > len(text) + 1:
                self.current_page += 1
                refresh()

        def previous_page():
            if not self.current_page - 1 < 0:
                self.current_page -= 1
                refresh()

        self.window.withdraw()
        result_page = Tk()
        result_page.eval(f'tk::PlaceWindow {str(result_page)} center')
        result_page.config(padx=20, bg="#F0F8FF")
        result_page.title("Bible Dictionary")

        meaning_label1 = Label(result_page, bg="#F0F8FF", font=("Arial", 15, "bold italic"))
        result_scroll1 = ScrolledText(result_page, width=50, height=10, bd=0, font=("Arial", 8, "normal"),
                                      wrap="word")
        translate_label1 = Label(result_page, text="Tłumaczenie", bg="#F0F8FF", font=("Arial", 11, "italic bold"))
        translate_scroll1 = ScrolledText(result_page, width=50, height=10, bd=0, font=("Arial", 8, "normal"),
                                         wrap="word")

        next_button = ttk.Button(result_page, style="TButton", text="Nas")

        meaning_label1.grid(row=0, column=0, pady=15, columnspan=2)
        result_scroll1.grid(row=1, column=0, columnspan=2, pady=7)
        translate_label1.grid(row=2, column=0, columnspan=2, pady=7)
        translate_scroll1.grid(row=3, column=0, columnspan=2, pady=15)

        def close_win(e):
            result_page.destroy()
            self.window.deiconify()

        result_page.bind('<Escape>', lambda e: close_win(e))
