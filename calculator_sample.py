#calculator using python tkinter
from tkinter import *

#tk window
window=Tk()
window.geometry("400x400")
window.title("calculator")
window.configure(bg="#00004d")

screen = Entry(window, font=('arial', 17, 'bold'), width=28, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=5, pady=25,padx=(15, 10))
screen.bind("<Key>", lambda e: "break")     # Disable characters from keyboard
screen.insert(0, "0")

#row 1 buttons
seven_button=Button(window, text="7")
seven_button.grid(row=1, column=0)

eight_button=Button(window, text="8")
eight_button.grid(row=1, column=1)

nine_button=Button(window, text="9")
nine_button.grid(row=1, column=2)

plus_button=Button(window, text="+")
plus_button.grid(row=1, column=3)

#row 2
four_button=Button(window, text="4")
four_button.grid(row=2, column=0)

five_button=Button(window, text="5")
five_button.grid(row=2, column=1)

six_button=Button(window, text="6")
six_button.grid(row=2, column=2)

mul_button=Button(window, text="x")
mul_button.grid(row=2, column=3)

#row 3
one_button=Button(window, text="1")
one_button.grid(row=3, column=0)

two_button=Button(window, text="2")
two_button.grid(row=3, column=1)

three_button=Button(window, text="3")
three_button.grid(row=3, column=2)

div_button=Button(window, text="/")
div_button.grid(row=3, column=3)

#row 4
zero_button=Button(window, text="0")
zero_button.grid(row=4, column=0,columnspan=2)

dot_button=Button(window, text=".")
dot_button.grid(row=4, column=2)

minus_button=Button(window, text="-")
minus_button.grid(row=4, column=3)


#row 5
clear_button=Button(window, text="clear")
clear_button.grid(row=5, column=0,columnspan=2)

equal_button=Button(window, text="=")
equal_button.grid(row=5, column=2,columnspan=2)


window.mainloop()