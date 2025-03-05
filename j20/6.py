from tkinter import *
from tkinter import messagebox


pin = input("enter your pin (4 digits): ")

if len(pin) != 4:
    messagebox.showerror("pin length", "pin must be 4 digits")
print("continue")