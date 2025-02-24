from tkinter import *


def test_function():
    lbl1.config(text="hello")


root = Tk()
root.title("first app")
root.config(background="orange")
root.geometry("300x300")

btn1 = Button(root, text="test button", command=lambda: test_function()).pack()
lbl1 = Label(root, text="")
lbl1.pack()

root.mainloop()