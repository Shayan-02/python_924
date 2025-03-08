from tkinter import messagebox
class CustomError(Exception):
    pass


pin = input("ramz e kart e khod ra vared konid: ")

if len(pin) != 4:
    # raise CustomError("tool e ramz e kart bayad 4 ragham bashad")
    messagebox.showerror("tool e ramz", "tool e ramz e kart bayad 4 ragham bashad")
else:
    print("ramz ok ast.")
