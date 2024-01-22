import tkinter as tk
from tkinter import simpledialog

#pseudocode
#accept string
string_var = tk.simpledialog.askstring("Hello", "Input your sentence: ")
find_string = tk.simpledialog.askstring("Hello", "What do you want to find? ")
#use .count() function
count = string_var.count(find_string)
#print result
print(find_string," appeared ",count, " times.")