# This is a GUI based simple calculator
from tkinter import *
win=Tk()
win.geometry('600x300')
win.title('Simple Calculator')
#Functions
def add():
 x=int(n1.get())
 y=int(n2.get())
 res=x+y
 lblres.config(text=str(x)+'+'+str(y)+'='+str(res))
def sub():
 x=int(n1.get())
 y=int(n2.get())
 res=x-y
 lblres.config(text=str(x)+'-'+str(y)+'='+str(res))
def mult():
 x=int(n1.get())
 y=int(n2.get())
 res=x*y
 lblres.config(text=str(x)+'*'+str(y)+'='+str(res))
def div():
 x=int(n1.get())
 y=int(n2.get())
 res=x/y
 lblres.config(text=str(x)+'/'+str(y)+'='+str(res))
#Label
lbln1=Label(win,text='Enter First No',fg='blue',font=('Arial',20))
lbln1.place(x=50,y=50)
lbln2=Label(win,text='Enter Second No',fg='blue',font=('Arial',20))
lbln2.place(x=50,y=100)
lblres=Label(win,text='Result',fg='blue',font=('Arial',20))
lblres.place(x=50,y=150)

#Entry
n1=StringVar()
entn1=Entry(win,bg='red',fg='white',font=('Arial',15),textvariable=n1,bd=5)
entn1.place(x=300,y=50)
n2=StringVar()
entn2=Entry(win,bg='red',fg='white',font=('Arial',15),textvariable=n2,bd=5)
entn2.place(x=300,y=100)
#Button
btnadd=Button(win,text='Add',fg='blue',font=('Arial',10),command=add)
btnadd.place(x=50,y=200)
btnsub=Button(win,text='Sub',fg='blue',font=('Arial',10),command=sub)
btnsub.place(x=150,y=200)
btnmult=Button(win,text='Mult',fg='blue',font=('Arial',10),command=mult)
btnmult.place(x=250,y=200)
btndiv=Button(win,text='Div',fg='blue',font=('Arial',10),command=div)
btndiv.place(x=350,y=200)
win.mainloop()