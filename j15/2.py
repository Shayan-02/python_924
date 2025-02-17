from pydoc import text
from tkinter import *


def show_fullName():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullName = fname + " " + lname
    fullName_lbl.config(text=f'نام کامل شما {fullName} است')

arman = Tk()
arman.title("fullname app")
arman.geometry("400x400")
arman.resizable(0, False)
# arman.config(bg="#f5d5a5")


defult_font = ('vazir', 16, 'bold')

fname_lbl = Label(arman, text="نام", padx=20, font=(("vazir", 16, "bold"))).grid(row=0, column=0)
fname_ent = Entry(arman, width=20, font=(("vazir", 14)))
fname_ent.grid(row=0, column=1)
lname_lbl = Label(
    arman, text="نام خانوادگی", padx=10, font=(("vazir", 16, "bold"))
).grid(row=1, column=0)
lname_ent = Entry(arman, width=20, font=(("vazir", 14)))
lname_ent.grid(row=1, column=1)
fullName_btn = Button(
    arman, text="submit", font=(("arial", 20, "bold")), bg="lightgreen", command=lambda:show_fullName()
).grid(row=2, column=1)
fullName_lbl = Label(arman, text="", font=(defult_font))
fullName_lbl.grid(row=3, column=1)
arman.mainloop()
