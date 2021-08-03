from tkinter import *
from tkinter import messagebox          # messagebox is used to show the message
import math

screen=Tk()

screen.geometry("362x500")              # it is uesd to fix the size of the app
screen.configure(bg='#254db2')          # it set the background color
screen.maxsize(width=453, height=510)   # it set the maximum size of the window
screen.minsize(width=362, height=510)   # it set the minimum size of the window
screen.title("Calculator")              # it give tittle to the window
screen.iconbitmap('cal.ico')            # it give icon image 


# Defining functions for a button  

def click(number):                      
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def singalclear():
    global operator
    result = list(operator)
    operator = result[:-1]
    tex.set(operator)

def equal():
    try:
        global operator
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification' ,'try again something went wrong here', parent=screen)

def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','try again something went wrong here',parent=screen)

def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','try again something went wrong here',parent=screen)

def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','try again something went wrong here',parent=screen)

def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','try again something went wrong here',parent=screen)

def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','try again something went wrong here',parent=screen)



# HOVER EFFECT FOR THR BUTTONS 

def on_entersin(e):
    btnsin.configure(bg='red')
def on_leavesin(e):
    btnsin.configure(bg='powder blue')

def on_entercos(e):
    btncos.configure(bg='red')
def on_leavecos(e):
    btncos.configure(bg='powder blue')

def on_entertan(e):
    btntan.configure(bg='red')
def on_leavetan(e):
    btntan.configure(bg='powder blue')

def on_entersqrt(e):
    btnsqrt.configure(bg='red')
def on_leavesqrt(e):
    btnsqrt.configure(bg='powder blue')

def on_enterlog(e):
    btnlog.configure(bg='red')
def on_leavelog(e):
    btnlog.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='red')
def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='red')
def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter7(e):
    btn7.configure(bg='red')
def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='red')
def on_leave6(e):
    btn6.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='red')
def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='red')
def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='red')
def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='red')
def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='red')
def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='red')
def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enteradd(e):
    btnadd.configure(bg='red')
def on_leaveadd(e):
    btnadd.configure(bg='powder blue')

def on_entermin(e):
    btnmin.configure(bg='red')
def on_leavemin(e):
    btnmin.configure(bg='powder blue')

def on_entermul(e):
    btnmul.configure(bg='red')
def on_leavemul(e):
    btnmul.configure(bg='powder blue')

def on_enterdiv(e):
    btndiv.configure(bg='red')
def on_leavediv(e):
    btndiv.configure(bg='powder blue')

def on_enterdot(e):
    btndot.configure(bg='red')
def on_leavedot(e):
    btndot.configure(bg='powder blue')



# DEFINING THE BUTTONS 

tex = StringVar()
operator = ''

entry1 = Entry(screen ,bg='gray',font=('arial',20,'italic bold'),bd='30',justify='right', textvariable=tex)
entry1.grid(row=0,columnspan=4)

btnAllClear= Button(screen, text='AC',font=('bold ,arial',20),bg="#F26E31",bd=8,padx=40,pady=8,activebackground='#254db2',activeforeground='white',command=lambda:clear())
btnAllClear.grid(row=1, column=2,columnspan=2)

btnClear= Button(screen, text='C',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:singalclear())
btnClear.grid(row=1, column=1)

btn7= Button(screen, text='7',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue", activebackground='#254db2',activeforeground='white',command=lambda:click(7))
btn7.grid(row=2, column=0)  

btn8= Button(screen, text='8',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(8))
btn8.grid(row=2, column=1)

btn9= Button(screen, text='9',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(9) )
btn9.grid(row=2, column=2)

btnadd= Button(screen, text='+',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click('+'))
btnadd.grid(row=2, column=3)

btn4= Button(screen, text='4',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(4))
btn4.grid(row=3, column=0)

btn5= Button(screen, text='5',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(5) )
btn5.grid(row=3, column=1)

btn6= Button(screen, text='6',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(6) )
btn6.grid(row=3, column=2)

btnmin= Button(screen, text='-',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click('-'))
btnmin.grid(row=3, column=3)

btn1= Button(screen, text='1',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(1))
btn1.grid(row=4, column=0)

btn2= Button(screen, text='2',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(2))
btn2.grid(row=4, column=1)

btn3= Button(screen, text='3',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(3) )
btn3.grid(row=4, column=2)

btnmul= Button(screen, text='*',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click('*'))
btnmul.grid(row=4, column=3)

btndot= Button(screen, text='.',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click('.'))
btndot.grid(row=5, column=0)

btn0= Button(screen, text='0',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click(0))
btn0.grid(row=5, column=1)

btndiv= Button(screen, text='/',font=('bold ,arial',20),bd=8,padx=8,pady=8 ,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:click('%'))
btndiv.grid(row=5, column=2)

btnequalto= Button(screen, text='=',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=lambda:equal() )
btnequalto.grid(row=5, column=3)

btnsin= Button(screen, text='sin',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=cmsin )
btnsin.grid(row=1, column=4)

btncos= Button(screen, text='cos',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=cmcos )
btncos.grid(row=2, column=4)

btntan= Button(screen, text='tan',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=cmtan )
btntan.grid(row=3, column=4)

btnsqrt= Button(screen, text='sqrt',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=cmsqrt )
btnsqrt.grid(row=4, column=4)

btnlog= Button(screen, text='log',font=('bold ,arial',20),bd=8,padx=8,pady=8,bg="powder blue",activebackground='#254db2',activeforeground='white',command=cmlog )
btnlog.grid(row=5, column=4)



# Binding for hover effect 

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btnmin.bind('<Enter>',on_entermin)
btnmin.bind('<Leave>',on_leavemin)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)



# Ending the window 
screen.mainloop()