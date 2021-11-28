from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk, IntVar, EW
import tkinter
import time
from translate import Translator

dicts = [
        "http://biblia-online.pl/Slownik/Biblijny/JamesStrongHebrew",
        "http://biblia-online.pl/Slownik/Biblijny/JamesStrongGreek",
        "http://biblia-online.pl/Slownik/Biblijny/EastonsBibleDictionary",
        "http://biblia-online.pl/Slownik/Biblijny/HitchcocksBibleNames",
        "http://biblia-online.pl/Slownik/Biblijny/KingJamesDictionary",
        "http://biblia-online.pl/Slownik/Biblijny/SmithsBibleDictionary"
    ]

chrome_options = Options()
chrome_options.add_argument("--headless")
current_item = 0


def result_window(znaczenia, link, number):
    translator = Translator(to_lang="pl")

    def refresh():
        matches_label.config(text=f"W tym słowniku znaleziono haseł - {number}")
        meaning_label1.config(text=dicts[current_item].split("/")[-1])
        result_scroll1.delete("1.0", "end")
        result_scroll1.insert("end", znaczenia[current_item])
        translate_scroll1.delete("1.0", "end")
        translate_scroll1.insert("1.0", translator.translate(znaczenia[current_item]))

    def next_page():
        global current_item
        new_num = current_item + 1
        if 0 <= new_num <= len(znaczenia) - 1:
            current_item = new_num
            refresh()

    def previous_page():
        global current_item
        new_num = current_item - 1
        if 0 <= new_num <= len(znaczenia) - 1:
            current_item = new_num
            refresh()

    result_page = tkinter.Toplevel(window)
    result_page.config(padx=20, bg="#F0F8FF")
    result_page.title("Results")

    meaning_label1 = ttk.Label(result_page, text="James Strong Hebrew", style="TLabel")
    result_scroll1 = ScrolledText(result_page, width=50, height=10, bd=0, font=("Arial", 8, "normal"), wrap="word")
    translate_label1 = ttk.Label(result_page, text="Tłumaczenie", style="TLabel")
    translate_scroll1 = ScrolledText(result_page, width=50, height=10, bd=0, font=("Arial", 8, "normal"), wrap="word")
    button_next = ttk.Button(result_page, text="Następny", command=next_page)
    button_previous = ttk.Button(result_page, text="Poprzedni", command=previous_page)
    matches_label = ttk.Label(result_page, text=f"{current_item + 1}/{len(znaczenia)}")
    link_label = ttk.Label(result_page, text="Link do wszystkich znalezionych haseł w słowniku\n" + link)

    link_label.grid(row=4, column=0, columnspan=2, pady=20)
    matches_label.grid(row=0, column=1)
    meaning_label1.grid(row=0, column=0, pady=15)
    result_scroll1.grid(row=1, column=0, columnspan=2)
    translate_label1.grid(row=2, column=0, columnspan=2, pady=15)
    translate_scroll1.grid(row=3, column=0, columnspan=2)
    button_next.grid(row=5, column=1, pady=20)
    button_previous.grid(row=5, column=0)

    refresh()

    result_page.mainloop()


def search(selected):
    word = search_field.get()
    with webdriver.Chrome(options=chrome_options) as driver:
        result = []
        for option in selected:
            driver.get(dicts[option])
            if option <= 1:
                keyword1 = "jstrong"
                keyword2 = "7"
                keyword3 = ".col-lg-4 a"
                keyword4 = "js-"
            elif option == 3:
                keyword1 = "dict"
                keyword2 = "2"
                keyword3 = ".col-lg-11 a"
                keyword4 = ""
            else:
                keyword1 = "dict"
                keyword2 = "2"
                keyword3 = ".col-lg-6 a"
                keyword4 = ""
            select = Select(driver.find_element(By.CSS_SELECTOR, f"#{keyword1}-field-id"))
            select.select_by_value(keyword2)
            pole_wyszukiwania = driver.find_element(By.CSS_SELECTOR, f"#{keyword1}-key")
            pole_wyszukiwania.send_keys(word)
            przycisk = driver.find_element(By.CSS_SELECTOR, f"#{keyword1}-search-submit")
            przycisk.click()
            time.sleep(1)
            link_result = driver.current_url
            wyniki = driver.find_element(By.CSS_SELECTOR, ".col-lg-4 span").text[-1]
            if int(wyniki) > 0:
                matches = driver.find_elements(By.CSS_SELECTOR, ".col-lg-1 a" if keyword4 == "js-" else keyword3)
                words_count = 0
                if int(wyniki) > 1:
                    anchors = []
                    result2 = ""
                    for match in matches:
                        anchors.append(match.get_attribute("href"))
                    for anchor in anchors:
                        driver.get(anchor)
                        result2 += f"{anchors.index(anchor) + 1}. Znalezione hasło w słowniku\n\n" + driver.find_element(By.CSS_SELECTOR, f".{keyword4}dict-desc").text + "\n\n"
                    result.append(result2)
                    words_count += len(matches)
                else:
                    print(len(matches))
                    matches[0].click()
                    result.append(f"1. Znalezione hasło w słowniku\n\n" + driver.find_element(By.CSS_SELECTOR, f".{keyword4}dict-desc").text + "\n\n")
                    words_count += 1
            else:
                result.append("Brak")
    result_window(result, link_result, words_count)


def check_search_options():
    option_list = [hebrew, greek, eastons, hitchcocks, king, smiths]
    selected_dicts = []
    for option in option_list:
        if option.get() == 1:
            index = option_list.index(option)
            selected_dicts.append(index)
    search(selected_dicts)


# GUI Interface

window = tkinter.Tk()
window.config(padx=25, pady=15, bg="#F0F8FF")
window.title("Tłumaczenie")

style = ttk.Style()
style.configure("TButton", background="#F0F8FF", font=("Arial", 8, "normal"))
style.configure("TCheckbutton", background="#F0F8FF", font=("Arial", 8, "italic"))
style.configure("TEntry", background="#F0F8FF")
style.configure("TLabel", background="#F0F8FF", font=("Arial", 7, "italic"))

hebrew = IntVar()
greek = IntVar()
eastons = IntVar()
hitchcocks = IntVar()
king = IntVar()
smiths = IntVar()

search_field = ttk.Entry(window, style="TEntry")
search_button = ttk.Button(window, text="Szukaj", style="TButton", command=check_search_options)
checkbox_hebrew = ttk.Checkbutton(window, text="James Strong Hebrew", style="TCheckbutton", variable=hebrew)
checkbox_greek = ttk.Checkbutton(window, text="James Strong Greek", style="TCheckbutton", variable=greek)
checkbox_eastons = ttk.Checkbutton(window, text="Eastons Bible Dictionary", style="TCheckbutton", variable=eastons)
checkbox_hitchcocks = ttk.Checkbutton(window, text="Hitchcocks Bible Names", style="TCheckbutton", variable=hitchcocks)
checkbox_king = ttk.Checkbutton(window, text="King James Dictionary", style="TCheckbutton", variable=king)
checkbox_smiths = ttk.Checkbutton(window, text="Smiths Bible Dictionary", style="TCheckbutton", variable=smiths)

search_field.grid(row=0, column=0, padx=5)
search_button.grid(row=1, column=0, pady=10, rowspan=2)
checkbox_hebrew.grid(row=0, column=1, padx=5, sticky=EW)
checkbox_greek.grid(row=1, column=1, padx=5, sticky=EW)
checkbox_eastons.grid(row=2, column=1, padx=5, sticky=EW)
checkbox_hitchcocks.grid(row=0, column=2, padx=5, sticky=EW)
checkbox_king.grid(row=1, column=2, padx=5, sticky=EW)
checkbox_smiths.grid(row=2, column=2, padx=5, sticky=EW)

window.mainloop()
