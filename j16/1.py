from tkinter import *


def show_fullName():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullName_lbl.config(text=f"نام کامل شما {fname} {lname} است")

root = Tk()
root.title("fullname app")
root.geometry("400x500")
root.resizable(0, 0)

fname_lbl = Label(root, text="نام", font=(('vazir', 16, 'bold')))
fname_lbl.pack(pady=10)

fname_ent = Entry(root, font=(('vazir', 14)))
fname_ent.pack(pady=10)

lname_lbl = Label(root, text="نام خانوادگی", font=(("vazir", 16, "bold")))
lname_lbl.pack(pady=10)

lname_ent = Entry(root, font=(("vazir", 14)))
lname_ent.pack(pady=10)

fullName_btn = Button(root, text="نمایش نام کامل", bg="lightgreen", font=(('arial', 20, 'bold')), command=lambda:show_fullName())
fullName_btn.pack(pady=30)

fullName_lbl = Label(root, text="", font=(('arial', 16, 'bold')))
fullName_lbl.pack()

root.mainloop()
