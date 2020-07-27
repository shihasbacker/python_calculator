from tkinter import *
window=Tk()
window.geometry("500x500")
window.title("calculator")
window.configure(bg="red")
button=Button(text="ok",width=30,height=30)
label=Label(window,text="welcome")

def hello():
    print("button clicked")

button.pack()
label.pack()
window.mainloop()
