from tkinter import *
win=Tk()
win.geometry("900x400")
win.title("Calculator")
win.resizable(0,0)

 
def button_click(item):
    global exp
    exp=exp+str(item)
    input_text.set(exp)

def button_clear():
    global exp
    exp=""
    input_text.set("")
    
def button_equal():
    global exp
    result=str(eval(exp))
    input_text.set(result)
    exp=""
    
exp=""

input_text=StringVar() # gets instance of the input field

input_frame=Frame(win, width=300, height=50, bd=0, highlightbackground="black",highlightcolor="black",highlightthickness="20")
input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=("calibri",20,"bold"),textvariable=input_text,width=100, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

buttons_frame=Frame(win, width=300, height=200, bg="black")
buttons_frame.pack()

clearbutton=Button(buttons_frame, text="C", fg="Black",width=40,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
dividebutton=Button(buttons_frame,text="/", fg="Black",width=20,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:button_click("/")).grid(row=0,column=3,padx=1,pady=1)

numseven=Button(buttons_frame,text="7",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(7)).grid(row=1,column=0,padx=1,pady=1)
numeight=Button(buttons_frame,text="8",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(8)).grid(row=1,column=1,padx=1,pady=1)
numnine=Button(buttons_frame,text="9",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(9)).grid(row=1,column=2,padx=1,pady=1)
multiplybutton=Button(buttons_frame,text="*",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("*")).grid(row=1,column=3,padx=1,pady=1)

numfour=Button(buttons_frame,text="4",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(4)).grid(row=2,column=0,padx=1,pady=1)
numfive=Button(buttons_frame,text="5",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(5)).grid(row=2,column=1,padx=1,pady=1)
numsix=Button(buttons_frame,text="3",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(3)).grid(row=2,column=2,padx=1,pady=1)
subtractbutton=Button(buttons_frame,text="-",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("-")).grid(row=2,column=3,padx=1,pady=1)

numthree=Button(buttons_frame,text="3",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(3)).grid(row=3,column=0,padx=1,pady=1)
numtwo=Button(buttons_frame,text="2",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(2)).grid(row=3,column=1,padx=1,pady=1)
numone=Button(buttons_frame,text="1",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(1)).grid(row=3,column=2,padx=1,pady=1)
plusbutton=Button(buttons_frame,text="+",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click("+")).grid(row=3,column=3,padx=1,pady=1)

numzero=Button(buttons_frame,text="0",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(0)).grid(row=4,column=0,padx=1,pady=1)
decimalbutton=Button(buttons_frame,text=".",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_click(".")).grid(row=4,column=1,padx=1,pady=1)
buttonequal=Button(buttons_frame,text="=",fg="Black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:button_equal()).grid(row=4,column=2,padx=1,pady=1)



win.mainloop()
