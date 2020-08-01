#calculator using python tkinter
from tkinter import *

#tk window
window=Tk()
window.geometry("420x330")
window.title("calculator")
window.configure(bg="#00004d")

text_in = StringVar()

operator = ""

#screen
screen= Entry(window,width=40,justify=RIGHT,textvar = text_in)
screen.grid(row=0, column=0, columnspan=4)
screen.bind("<Key>", lambda e: "break")


# function to update operator in the entry field
def click_button(number):
    global operator
    operator = operator + str(number)
    # update the operator using set method
    text_in.set(operator)

def eql_button():
    global operator
    # we using eval function for evaluate operator
    total = str(eval(operator))
    text_in.set(total)
    # initialize the operator variable by empty string
    operator = ""


# function for substraction
def sub_button():
    global operator
    sub = str(eval(operator))
    text_in.set(sub)
    operator = ""


# function for multiplication
def mul_button():
    global operator
    mul = str(eval(operator))
    text_in.set(mul)
    operator = ""


# function for division
def div_button():
    global operator
    div = str(eval(operator))
    text_in.set(div)
    operator = ""


# function for clear entry field
def clr_button():
    global operator
    operator = ""
    text_in.set("")

#row 1 buttons
seven_button=Button(window, text="7",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(7))
seven_button.grid(row=1, column=0)

eight_button=Button(window, text="8",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(8))
eight_button.grid(row=1, column=1)

nine_button=Button(window, text="9",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(9))
nine_button.grid(row=1, column=2)

plus_button=Button(window, text="+",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button("+"))
plus_button.grid(row=1, column=3)

#row 2
four_button=Button(window, text="4",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(4))
four_button.grid(row=2, column=0)

five_button=Button(window, text="5",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(5))
five_button.grid(row=2, column=1)

six_button=Button(window, text="6",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(6))
six_button.grid(row=2, column=2)

mul_button=Button(window, text="x",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button("*"))
mul_button.grid(row=2, column=3)

#row 3
one_button=Button(window, text="1",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(1))
one_button.grid(row=3, column=0)

two_button=Button(window, text="2",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(2))
two_button.grid(row=3, column=1)

three_button=Button(window, text="3",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(3))
three_button.grid(row=3, column=2)

div_button=Button(window, text="/",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button("/"))
div_button.grid(row=3, column=3)

#row 4
zero_button=Button(window, text="0",bd=4,height=2,width=16,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button(0))
zero_button.grid(row=4, column=0,columnspan=2)

dot_button=Button(window, text=".",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button("."))
dot_button.grid(row=4, column=2)

minus_button=Button(window, text="_",bd=4,height=2,width=6,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: click_button("-"))
minus_button.grid(row=4, column=3)


#row 5
clear_button=Button(window, text="clear",bd=4,height=2,width=16,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=lambda: clr_button())
clear_button.grid(row=5, column=0,columnspan=2)

equal_button=Button(window, text="=",bd=4,height=2,width=16,fg="#ffffff",bg="#006680", activebackground="#66e0ff",command=eql_button)
equal_button.grid(row=5, column=2,columnspan=2)



window.mainloop()