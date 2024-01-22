import tkinter as tk
from tkinter import simpledialog

string_var = tk.simpledialog.askstring("Hello", "Input your sentence: ")
find_string = tk.simpledialog.askstring("Hello", "What do you want to find? ")
count = string_var.count(find_string)
print(find_string," appeared ",count, " times.")
