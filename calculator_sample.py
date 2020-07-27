#calculator using python tkinter
from tkinter import *

#tk window
window=Tk()
window.geometry("500x500")
window.title("calculator")
window.configure(bg="#00004d")

screen = Entry(window, font=('arial', 17, 'bold'), width=28, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=5, pady=1)
screen.bind("<Key>", lambda e: "break")     # Disable characters from keyboard
screen.insert(0, "0")

window.mainloop()