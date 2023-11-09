import tkinter as tk


def menu_new_file():
    window['bg'] = 'black'


def menu_open():
    window['bg'] = 'yellow'


def menu_save():
    window['bg'] = 'red'
    print('Save ... selected')


def menu_save_as():
    window['bg'] = 'blue'
    # print('Save As... selected')


def menu_exit():
    window['bg'] = 'green'
    # print('Exit selected')


window = tk.Tk()
menubar = tk.Menu(window)
dropdown_menu = tk.Menu(menubar, tearoff=0)
dropdown_menu.add_command(label='New File', command=menu_new_file)
dropdown_menu.add_command(label='Open', command=menu_open)
dropdown_menu.add_separator()
dropdown_menu.add_command(label='Save', command=menu_save)
dropdown_menu.add_command(label='Save As', command=menu_save_as)
dropdown_menu.add_separator()
dropdown_menu.add_command(label='Exit', command=menu_exit)
menubar.add_cascade(label='File', menu=dropdown_menu)
window.config(menu=menubar)


window.mainloop()