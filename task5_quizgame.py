from tkinter import *

win=Tk()
ico=PhotoImage(file='images.png')
win.iconphoto(False,ico)
win.geometry("800x600+30+40")
win.title("QUIZ GAME")
win.resizable(False,False)

frame1=Frame(win,relief=RIDGE,borderwidth=2,bg="red")
frame1.place(x=0,y=0,height=70,width=800)

title=Label(frame1,text="COMPUTER QUIZ GAME",font=("times new roman",35,"bold"),bg="red",
            fg="white")
title.pack(side=TOP,fill=BOTH)
title.config(pady=10)

questions=[{
       "question": "Q-1) MS-Word is an example of _____",
       "options":["An operating system","A Processing Unit","Application Software","An Input device"],
       "answer":"Application Software"
    },
    {
        "question":"Q-2) A computer cannot boot if it does not have the _____",
        "options":["Compiler","Loader","Assembler","Operating System"],
        "answer":"Operating System"
    },
    {
        "question":"Q-3) ________ is the process of dividing the disk into tracks and sectors",
        "options":["Tracking","Formatting","Caching","Allocating"],
        "answer":"Formatting"
    },
    {
        "question":"Q-4) Ctrl, Shift and Alt are called .......... keys.",
        "options":["modifier","function","alphanumeric","adjustment"],
        "answer":"modifier"
    },
    {
        "question":"Q-5) Junk e-mail is also called ______",
        "options":["Spam","Spoof","Spool","Sniffer Script"],
        "answer":"Spam"
    },
    {
        "question":"Q-6) Microsoft Office is an example of a",
        "options":["Closed source software","Open source software","Horizontal market software","vertical market software"],
        "answer":"Horizontal market software"
    },
    {
        "question":"Q-7) _____are attempts by individuals to obtain confidential information from you by falsifying their identity",
        "options":["Phising","Sniffing","Reverse Engineering","Malware"],
        "answer":"Phising"
    },
    {
        "question":"Q-8) Which one is not a linear data Structure",
        "options":["Array","Linked List","Stack","Graph"],
        "answer":"Graph"
    },
    {
        "question":"Q-9) What is the binary form of 29",
        "options":["11101","01101","11110","10101"],
        "answer":"11101"
    },
    {
        "question":"Q-10) What is not a type of loop in C++ Programming Language",
        "options":["for","while","do-while","if-else"],
        "answer":"if-else"
    }
]



frame3=Frame(win,relief=RIDGE,borderwidth=2)
frame3.place(x=500,y=70,height=530,width=300)


win.mainloop()