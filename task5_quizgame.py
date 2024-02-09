from tkinter import *

win=Tk()

ico=PhotoImage(file='images.png')
win.iconphoto(False,ico)
win.geometry("1000x650+40+30")
win.title("QUIZ GAME")
win.resizable(False,False)

frame1=Frame(win)
frame1.place(x=0,y=0,width=1000,height=60)

heading=Label(frame1,text="COMPUTER QUIZ GAME",font=("times new roman",30,"bold"),fg="white",
              bg="red",relief=FLAT,borderwidth=6)
heading.pack(side=TOP,fill=X)

frame2=Frame(win,bg="red")
frame2.place(x=0,y=60,width=600,height=590)

frame3=Frame(win,bg="black")
frame3.place(x=600,y=60,width=400,height=590)

win.mainloop()

