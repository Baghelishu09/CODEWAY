from tkinter import *
import json
import requests

win=Tk()
win.title("WEATHER FORECAST APP")
win.geometry("400x500+0+0")
win.resizable(False,False)

input_label=Label(win,text="Enter city name : ",font=("Calbari",14,"italic"))
input_label.place(x=15,y=20)

input_field=Entry(win,font=("times new roman",12),relief=RIDGE,borderwidth=3)
input_field.place(x=170,y=20,height=30,width=200)

btn=Button(text="SUBMIT",relief=RAISED,font=("times new roman",12,"bold"),
           borderwidth=2,bg="green",fg="white")
btn.place(x=160,y=75)

ico=PhotoImage(file='weather.png')
win.iconphoto(False,ico)


win.mainloop()

