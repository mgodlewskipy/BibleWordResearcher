import tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from search_in_dictionary import SearchInDict

dict_list = ["Easton's Bible Dictionary", "Hitchcock's Names Dictionary", "Naves Topical Index",
             "Smith's Bible Dictionary", "Webster's 1828 Dictionary"]

LIST = [
        ["Webster's 1828 Dictionary", 1],
        ["Smith's Bible Dictionary", 1],
        ["Easton's Bible Dictionary", 1],
        ["Hitchcock's Names Dictionary", 1],
        ["Naves Topical Index", 1],
        ["ball", 1],
    ]

current_page = 0
condition = True


def result_frame(options):
    global condition

    def refresh():
        try:
            dict_title.config(text=f"{text[current_page][0]}")
            left_box.delete("1.0", "end")
            right_box.delete("1.0", "end")
            left_box.insert("end", text[current_page][1])
            right_box.insert("end", translated[current_page])
        except IndexError:
            dict_title.config(text="Nie można zlokalizować żródła")
            left_box.delete("1.0", "end")
            right_box.delete("1.0", "end")

    def next_page():
        global current_page
        if not current_page + 1 > len(text) - 1:
            current_page += 1
            refresh()

    def previous_page():
        global current_page
        if not current_page - 1 < 0:
            current_page -= 1
            refresh()

    if condition:
        main_frame.destroy()
        condition = False

    result_frame_section.pack(fill="both", expand=True)

    result_frame_section.create_image(70, 90, image=result_bg, anchor="nw")
    result_frame_section.create_image(450, 90, image=result_bg, anchor="nw")

    next_button.place(x=535, y=530)
    previous_button.place(x=140, y=530)

    left_box.place(x=78, y=100)

    right_box.place(x=458, y=100)

    dict_title.place(x=295, y=38)

    next_button.config(command=next_page)
    previous_button.config(command=previous_page)

    my_search = SearchInDict(options, s_entry.get())
    text = my_search.result_in_en
    translated = my_search.result_in_pl

    refresh()

    return 0


def search_button_clicked():
    word = s_entry
    if LIST[-1][1] == -1:
        selected_options = dict_list
    else:
        selected_options = [option[0] for option in LIST if option[1] == -1]

    if not len(selected_options) == 0 and not word == "":
        result_frame(selected_options)


def button_clicked(button, name_c, name_nt, name):
    global LIST

    def reset_buttons():
        button_naves.config(image=naves_img)
        button_webster.config(image=webster_img)
        button_smith.config(image=smith_img)
        button_hitch.config(image=hitch_img)
        button_easton.config(image=easton_img)

        for item_b in LIST[:5]:
            item_b[1] = 1

    if name == "ball" and LIST[-1][1] == 1:
        reset_buttons()

    if not LIST[-1][1] == -1 or name == "ball":
        for item in LIST:
            if item[0] == name:
                index = LIST.index(item)

        LIST[index][1] *= -1

        if LIST[index][1] == 1:
            button.config(image=name_nt)
        else:
            button.config(image=name_c)


root = Tk()
root.geometry("813x724")
root.config(bg="#ffffff")
root.title("Bible Dictionary")
root.resizable(False, False)
root.attributes("-topmost", True)
root.update()

# Creating top panel

bg = PhotoImage(file="images/img.png")

ball_img = PhotoImage(file="images/ball.png")
webster_img = PhotoImage(file="images/webster.png")
smith_img = PhotoImage(file="images/smith.png")
easton_img = PhotoImage(file="images/easton.png")
hitch_img = PhotoImage(file="images/hitch.png")
naves_img = PhotoImage(file="images/naves.png")
srectangle_img = PhotoImage(file="images/srectangle.png")
sbutton_img = PhotoImage(file="images/sbutton.png")
result_bg = PhotoImage(file="images/result_img.png")
top_brown_img = PhotoImage(file="images/top_brown.png")

ball_img_c = PhotoImage(file="images/ball_c.png")
webster_img_c = PhotoImage(file="images/webster_c.png")
smith_img_c = PhotoImage(file="images/smith_c.png")
easton_img_c = PhotoImage(file="images/easton_c.png")
hitch_img_c = PhotoImage(file="images/hitch_c.png")
naves_img_c = PhotoImage(file="images/naves_c.png")
next_img = PhotoImage(file="images/next.png")
previous_img = PhotoImage(file="images/previous.png")

top_panel_canvas = Canvas(root, width=813, height=116, bg="#ffffff", bd=0, highlightthickness=0)
top_panel_canvas.pack(fill="both", expand=True)
top_panel_canvas.create_image(0, 0, image=top_brown_img, anchor="nw")
top_panel_canvas.create_image(0, 5, image=bg, anchor="nw")

search_place = Canvas(top_panel_canvas, bg="#F6F6F6", width=160, height=32, bd=0, highlightthickness=0)
search_place.place(x=20, y=16)

search_place.create_image(80, 21, image=srectangle_img)

sbutton = Button(search_place, image=sbutton_img, bg="#F6F6F6", width=25, height=22, bd=0, highlightthickness=0, cursor="hand2", command=search_button_clicked, activebackground="#F6F6F6")
sbutton.place(x=122, y=6)

s_entry = Entry(search_place,  bg="#F6F6F6", bd=0, highlightthickness=0, width=17, fg="#6F6F6F", font=("Arial", 8, "normal"))
s_entry.place(x=13, y=8)
s_entry.focus_set()

button_all = Button(top_panel_canvas, image=ball_img, bg="#F6F6F6", width=154, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_all, ball_img_c, ball_img, "ball"), cursor="hand2", activebackground="#F6F6F6")
button_all.place(x=190, y=21)

button_webster = Button(top_panel_canvas, image=webster_img, bg="#F6F6F6", width=222, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_webster, webster_img_c, webster_img, "Webster's 1828 Dictionary"), cursor="hand2", activebackground="#F6F6F6")
button_webster.place(x=355, y=21)

button_smith = Button(top_panel_canvas, image=smith_img, bg="#F6F6F6", width=197, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_smith, smith_img_c, smith_img, "Smith's Bible Dictionary"), cursor="hand2", activebackground="#F6F6F6")
button_smith.place(x=590, y=21)

button_easton = Button(top_panel_canvas, image=easton_img, bg="#F6F6F6", width=199, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_easton, easton_img_c, easton_img, "Easton's Bible Dictionary"), cursor="hand2", activebackground="#F6F6F6")
button_easton.place(x=20, y=60)

button_hitch = Button(top_panel_canvas, image=hitch_img, bg="#F6F6F6", width=232, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_hitch, hitch_img_c, hitch_img, "Hitchcock's Names Dictionary"), cursor="hand2", activebackground="#F6F6F6")
button_hitch.place(x=230, y=60)

button_naves = Button(top_panel_canvas, image=naves_img, bg="#F6F6F6", width=211, height=32, bd=0, highlightthickness=0, command=lambda: button_clicked(button_naves, naves_img_c, naves_img, "Naves Topical Index"), cursor="hand2", activebackground="#F6F6F6")
button_naves.place(x=475, y=60)

# Creating main panel
home_img = PhotoImage(file="images/text_home_page.png")

main_frame = Canvas(root, width=813, height=724-116, bg="#ffffff", bd=0, highlightthickness=0)
main_frame.pack(fill="both", expand=True)

main_frame.create_image(180, 70, image=home_img, anchor="nw")

root.bind('<Return>', lambda event=None: sbutton.invoke())

# results

result_frame_section = Canvas(root, width=813, height=724 - 116, bg="#ffffff", bd=0, highlightthickness=0)
next_button = Button(result_frame_section, image=next_img, bg="#ffffff", width=139, height=32, bd=0,
                     highlightthickness=0, cursor="hand2", activebackground="#ffffff")
previous_button = Button(result_frame_section, image=previous_img, bg="#ffffff", width=139, height=32, bd=0,
                         highlightthickness=0, cursor="hand2", activebackground="#ffffff")
left_box = ScrolledText(result_frame_section, wrap=tkinter.WORD, width=44, height=28,
                        font=("Arial", 8, "normal"), bd=0)
right_box = ScrolledText(result_frame_section, wrap=tkinter.WORD, width=44, height=28,
                         font=("Arial", 8, "normal"), bd=0)
dict_title = Label(result_frame_section, text="Hitchcock's Names Dictionary", fg="#6F6F6F",
                   font=("Arial", 14, "normal"), bg="#ffffff")

root.mainloop()
