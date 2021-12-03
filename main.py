import dane
from result_window import NewAppWindow
from search_in_dictionary import SearchInDict


def search():
    condition = False
    index = []
    for value in my_window.checkbutton_status:
        if value.get() == 1:
            index.append(my_window.checkbutton_status.index(value))
            condition = True
    if my_window.search_field.get() == "" or not condition:
        my_window.empty_entry_warning()
        return 0
    my_search = SearchInDict([dane.dict_list[title] for title in index], my_window.search_field.get())

    my_window.result_self_window(my_search.result_in_en, my_search.result_in_pl)


my_window = NewAppWindow()

my_window.add_options(dane.dict_list)
my_window.search_button.config(command=search)

my_window.window.mainloop()
