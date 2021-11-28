from tkinter import *
from tkinter.scrolledtext import ScrolledText
import webbrowser


class ResultPage:
    def __init__(self, desc, title, links):
        def callback(url):
            webbrowser.open_new_tab(url)

        def create_new_label(link):
            new_label = Label(new_window, text=link, fg="blue", bg="#F0F8FF", cursor="hand2", font=("Arial", 9, "underline"))
            new_label.pack(pady=10, anchor="w")
            new_label.bind("<Button-1>", lambda e: callback(link))

        new_window = Tk()
        new_window.config(padx=25, pady=15, bg="#F0F8FF")
        new_window.title(title)

        label_results = Label(new_window, text="Wyniki wyszukiwania", font=("Arial", 10, "italic"), bg="#F0F8FF")
        result_scroll = ScrolledText(new_window, width=80, height=10, bd=0, font=("Arial", 8, "normal"), wrap="word")
        translate_label = Label(new_window, text="Tłumaczenie", font=("Arial", 10, "italic"), bg="#F0F8FF")
        translate_scroll = ScrolledText(new_window, width=80, height=10, bd=0, font=("Arial", 8, "normal"), wrap="word")
        links_label = Label(new_window, text="Linki", font=("Arial", 10, "italic"), bg="#F0F8FF")

        label_results.pack(pady=5, anchor="w")
        result_scroll.pack(pady=5)
        translate_label.pack(pady=5, anchor="w")
        translate_scroll.pack(pady=5)
        links_label.pack(pady=5, anchor="w")

        result_scroll.insert("end", desc)

        for x in links:
            create_new_label(x)

        new_window.mainloop()
