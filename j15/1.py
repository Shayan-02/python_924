from tkinter import *


arman = Tk()
arman.title("fullname app")
arman.geometry("400x400")
arman.resizable(0, False)
# arman.config(bg="#f5d5a5")


fname_lbl = Label(arman, text="نام", pady=20, font=(('vazir', 16, 'bold'))).pack()
fname_ent = Entry(arman, width=20, font=(('vazir', 14))).pack()
lname_lbl = Label(arman, text="نام خانوادگی", pady=10, font=(('vazir', 16, 'bold'))).pack()
fname_ent = Entry(arman, width=20, font=(("vazir", 14))).pack()
fullName_btn = Button(arman, text="submit", font=(('arial', 20, 'bold')), bg="lightgreen").pack()
arman.mainloop()
