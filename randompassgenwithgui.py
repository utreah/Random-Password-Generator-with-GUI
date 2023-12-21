import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
import random

button_check_list = []


def get_button_status_symbol():
    return symbol_variable.get()


def get_button_status_uppercase():
    return uppercase_variable.get()


def get_button_status_lowercase():
    return lowercase_variable.get()


def get_button_status_numbers():
    return number_variable.get()


def button_check_list_changed(unique_identifier):
    if unique_identifier in button_check_list:
        pass
    else:
        button_check_list.append(unique_identifier)


def create_random_password(password_length):
    password = ""
    for _ in range(password_length):
        if get_button_status_symbol():
            password += random.choice('!@#$%^&*()-_+=[]{}|;:\'",.<>?/')
            symbol_unique_word = "symbol"
            button_check_list_changed(symbol_unique_word)
        if get_button_status_uppercase():
            password += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            uppercase_unique_word = "uppercase"
            button_check_list_changed(uppercase_unique_word)
        if get_button_status_lowercase():
            password += random.choice('abcdefghijklmnopqrstuvwxyz')
            lowercase_unique_word = "lowercase"
            button_check_list_changed(lowercase_unique_word)
        if get_button_status_numbers():
            password += random.choice('0123456789')
            numbers_unique_word = "numbers"
            button_check_list_changed(numbers_unique_word)
    if not password:
        return "Choose at least one character type"
    if len(button_check_list) > 1:
        avg_index = len(password) // len(button_check_list)
        password_list = list(password)
        random.shuffle(password_list)
        password = password_list
        return ''.join(password[:avg_index])
    else:
        return password


def insert_to_textbox():
    generated_random_password = create_random_password(slider_variable.get())
    password_text_box.delete("1.0", tk.END)
    password_text_box.insert("1.0", generated_random_password)
    password_text_box.config(state=tk.DISABLED)


def copy_to_clipboard():
    generated_random_password = password_text_box.get(1.0, tk.END).strip()
    pyperclip.copy(generated_random_password)
    pyperclip.paste()
#    print(pyperclip.paste())
    messagebox.showinfo("Copied!", "Password copied to clipboard")


def get_slider_val(*args):
    value = format(slider_variable.get())
    password_length_slider_label.config(text=value)
#    print(value)
    password_text_box.config(state=tk.NORMAL)
    insert_to_textbox()

# Window GUI section
window = tk.Tk()
window.title("Random Password Generator")
window.resizable(False, False)   # window size can(not) be change.
# End

# get screen height and width by winfo_
get_screen_height = window.winfo_screenheight()
get_screen_width = window.winfo_screenwidth()
window_height = 200  # set window_y (size)
window_width = 350  # set window_x (size)
# End

# Calculations to get center of the screen
get_center_x = int((get_screen_width/2) - (window_width/2))
get_center_y = int((get_screen_height/2) - (window_height/2))
# End

window.geometry(f'{window_width}x{window_height}-{get_center_x}+{get_center_y}')  # set window to center of the screen

# Create a button
copy_generated_password = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_generated_password.pack()
copy_generated_password.place(x=window_width/2, y=window_height, anchor=tk.S)
# End

# Create a slider between min = 6 and max = 18
slider_variable = tk.IntVar()
password_length_slider = ttk.Scale(window, from_=6, to=18, orient='horizontal', command=get_slider_val, variable=slider_variable)
password_length_slider_label = ttk.Label(window, text="1")
password_length_slider_label.place(x=window_width-170, y=window_height-170, anchor=tk.NE)
password_length_slider.place(x=window_width/2, y=window_height/25, anchor=tk.N)
# End

# create checkbox for symbols
symbol_variable = tk.BooleanVar()
checkbox_symbols = ttk.Checkbutton(window, text="Symbols", onvalue=True, offvalue=False, command=get_button_status_symbol, variable=symbol_variable)
checkbox_symbols.place(x=window_width/18, y=window_height-10, anchor=tk.W)
# create checkbox for Uppercase
uppercase_variable = tk.BooleanVar()
checkbox_characters = ttk.Checkbutton(window, text="Uppercase", onvalue=True, offvalue=False, command=get_button_status_uppercase, variable=uppercase_variable)
checkbox_characters.place(x=window_width/18, y=window_height-30, anchor=tk.W)
# create checkbox for lowercase
lowercase_variable = tk.BooleanVar()
checkbox_characters = ttk.Checkbutton(window, text="Lowercasecase", onvalue=True, offvalue=False, command=get_button_status_lowercase, variable=lowercase_variable)
checkbox_characters.place(x=window_width/18, y=window_height-50, anchor=tk.W)
# create checkbox for numbers
number_variable = tk.BooleanVar()
checkbox_numbers = ttk.Checkbutton(window, text="Numbers", onvalue=True, offvalue=False, command=get_button_status_numbers, variable=number_variable)
checkbox_numbers.place(x=window_width/18, y=window_height-70, anchor=tk.W)
# Create a text box for random password to show
password_text_box = tk.Text(window, width=20, height=1)
password_text_box.place(x=window_width-255, y=window_height-130, anchor=tk.W)
# Run the main event loop
window.mainloop()
