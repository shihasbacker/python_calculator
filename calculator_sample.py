#calculator using python tkinter
from tkinter import *

#tk window
window=Tk()
window.geometry("430x340")
window.title("calculator")
window.configure(bg="#00004d")


#screen
screen= Entry(window,width=40,justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4,)
screen.bind("<Key>", lambda e: "break")

#row 1 buttons
seven_button=Button(window, text="7",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
seven_button.grid(row=1, column=0)

eight_button=Button(window, text="8",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
eight_button.grid(row=1, column=1)

nine_button=Button(window, text="9",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
nine_button.grid(row=1, column=2)

plus_button=Button(window, text="+",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
plus_button.grid(row=1, column=3)

#row 2
four_button=Button(window, text="4",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
four_button.grid(row=2, column=0)

five_button=Button(window, text="5",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
five_button.grid(row=2, column=1)

six_button=Button(window, text="6",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
six_button.grid(row=2, column=2)

mul_button=Button(window, text="x",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
mul_button.grid(row=2, column=3)

#row 3
one_button=Button(window, text="1",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
one_button.grid(row=3, column=0)

two_button=Button(window, text="2",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
two_button.grid(row=3, column=1)

three_button=Button(window, text="3",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
three_button.grid(row=3, column=2)

div_button=Button(window, text="/",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
div_button.grid(row=3, column=3)

#row 4
zero_button=Button(window, text="0",bd=4,height=2,width=18,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
zero_button.grid(row=4, column=0,columnspan=2)

dot_button=Button(window, text=".",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
dot_button.grid(row=4, column=2)

minus_button=Button(window, text="_",bd=4,height=2,width=7,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
minus_button.grid(row=4, column=3)


#row 5
clear_button=Button(window, text="clear",bd=4,height=2,width=16,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
clear_button.grid(row=5, column=0,columnspan=2)

equal_button=Button(window, text="=",bd=4,height=2,width=16,fg="#ffffff",bg="#006680", activebackground="#66e0ff")
equal_button.grid(row=5, column=2,columnspan=2)



window.mainloop()