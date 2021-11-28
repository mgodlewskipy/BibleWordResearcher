from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from tkinter import ttk
from tkinter import *
from resultpage import ResultPage


def search(options, word):
    if len(options) > 0:
        def james_strong():
            Select(driver.find_element(By.CSS_SELECTOR, "#jstrong-field-id")).select_by_value("7")
            driver.find_element(By.CSS_SELECTOR, "#jstrong-key").send_keys(word)
            driver.find_element(By.CSS_SELECTOR, "#jstrong-search-submit").click()
            title = driver.find_element(By.CSS_SELECTOR, ".vtbl-hdr").text
            matches = driver.find_elements(By.CSS_SELECTOR, ".col-lg-1 a")
            results = [match.get_attribute("href") for match in matches]
            if len(results) > 1:
                description = ""
                for item in results:
                    driver.get(item)
                    description += driver.find_element(By.CSS_SELECTOR, ".js-dict-desc").text + "\n\n\n"
            elif len(results) == 1:
                driver.get(results[0])
                description = driver.find_element(By.CSS_SELECTOR, ".js-dict-desc").text
            else:
                description = "Brak"
            ResultPage(description, title, results)

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        with webdriver.Chrome(options=chrome_options) as driver:
            for option in options:
                driver.get(option)
                if option.split("/")[-1] == "JamesStrongHebrew" or option.split("/")[-1] == "JamesStrongGreek":
                    james_strong()

                input()


# GUI Interface
def app():
    dicts = [
        "http://biblia-online.pl/Slownik/Biblijny/JamesStrongHebrew",
        "http://biblia-online.pl/Slownik/Biblijny/JamesStrongGreek",
        "http://biblia-online.pl/Slownik/Biblijny/EastonsBibleDictionary",
        "http://biblia-online.pl/Slownik/Biblijny/HitchcocksBibleNames",
        "http://biblia-online.pl/Slownik/Biblijny/KingJamesDictionary",
        "http://biblia-online.pl/Slownik/Biblijny/SmithsBibleDictionary"
    ]

    window = Tk()
    window.config(padx=25, pady=15, bg="#F0F8FF")
    window.title("Tłumaczenie")

    def check():
        return [dicts[available_options.index(option)] for option in available_options if option.get() == 1]

    available_options = [IntVar() for _ in range(6)]

    style = ttk.Style()
    style.configure("TButton", background="#F0F8FF", font=("Arial", 8, "normal"))
    style.configure("TCheckbutton", background="#F0F8FF", font=("Arial", 8, "italic"))
    style.configure("TEntry", background="#F0F8FF")
    style.configure("TLabel", background="#F0F8FF", font=("Arial", 7, "italic"))

    search_field = ttk.Entry(window, style="TEntry")
    search_button = ttk.Button(window, text="Szukaj", style="TButton", command=lambda: search(check(), search_field.get()))
    checkbox_hebrew = ttk.Checkbutton(window, text="James Strong Hebrew", style="TCheckbutton", variable=available_options[0])
    checkbox_greek = ttk.Checkbutton(window, text="James Strong Greek", style="TCheckbutton", variable=available_options[1])
    checkbox_eastons = ttk.Checkbutton(window, text="Eastons Bible Dictionary", style="TCheckbutton", variable=available_options[2])
    checkbox_hitchcocks = ttk.Checkbutton(window, text="Hitchcocks Bible Names", style="TCheckbutton", variable=available_options[3])
    checkbox_king = ttk.Checkbutton(window, text="King James Dictionary", style="TCheckbutton", variable=available_options[4])
    checkbox_smiths = ttk.Checkbutton(window, text="Smiths Bible Dictionary", style="TCheckbutton", variable=available_options[5])

    search_field.grid(row=0, column=0, padx=5)
    search_button.grid(row=1, column=0, pady=10, rowspan=2)
    checkbox_hebrew.grid(row=0, column=1, padx=5, sticky=EW)
    checkbox_greek.grid(row=1, column=1, padx=5, sticky=EW)
    checkbox_eastons.grid(row=2, column=1, padx=5, sticky=EW)
    checkbox_hitchcocks.grid(row=0, column=2, padx=5, sticky=EW)
    checkbox_king.grid(row=1, column=2, padx=5, sticky=EW)
    checkbox_smiths.grid(row=2, column=2, padx=5, sticky=EW)

    window.mainloop()


app()
