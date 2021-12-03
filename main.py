import dane
from result_window import NewAppWindow
from search_in_dictionary import SearchInDict


def search():
    condition = False
    for value in my_window.checkbutton_status:
        if value == 1:
            condition = True
    if my_window.search_field.get() == "" or not condition:
        my_window.empty_entry_warning()
        return 0
    print("lol")


my_window = NewAppWindow()

my_window.add_options(dane.dict_list)
my_window.search_button.config(command=search)

my_window.window.mainloop()
