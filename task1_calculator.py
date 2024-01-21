from tkinter import *

win = Tk()
win.geometry("300x400+0+0")
win.title("SIMPLE CALCULATOR")
win.resizable(False,False)
win.configure(background="white")

# functionality and logic
    

#result screen

result_scrn=Label(win,text=0,fg="black",bg="white")
result_scrn.grid(row=0,column=0)
result_scrn.config(font=("verdana",30,"bold"))

btn1 = Button(win,text='0',width=5,height=2,
              fg="grey",bg="white")
btn1.grid(row=1,column=0)
btn1.config(font=("calibri",15,"bold"))

win.mainloop()