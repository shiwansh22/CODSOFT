from tkinter import*
from tkinter import messagebox
import pyperclip
import random
import string
root=Tk()
root.geometry("900x600+350+80")
root.title("Password Generator")
root.config(bg="white smoke")
root.resizable(0,0)
#function
a=StringVar()
b=StringVar()
c=StringVar()
def gen():
    letters=string.ascii_letters
    di=string.digits
    alpha=letters+di
    p=int(b.get())
    pwd=''.join(random.choice(alpha)for i in range(p))
    
    c.set(pwd)
ent2=Entry(root,font=("Arial",17,"bold"),fg="black",borderwidth=5,textvariable=c)
ent2.place(x=320,y=350)

def acpt():
    pyperclip.copy(c.get())
    
    messagebox.showinfo("The password saved to clipboard")
def rjct():
    messagebox.showinfo("k")

#label
lb=Label(root,text="Password Generator",font=("Arial",25),fg="blue")
lb.place(x=320,y=10)

lb1=Label(root,text="Enter User name:",font=("Arial",17,"bold"),fg="black")
lb1.place(x=20,y=150)

lb2=Label(root,text="Enter password length:",font=("Arial",17,"bold"),fg="black")
lb2.place(x=10,y=250)

lb3=Label(root,text="Generated password:",font=("Arial",17,"bold"),fg="black")
lb3.place(x=20,y=350)

# lb4=Label(root,text="Password contains of uppercase, lowercase and digits only",font=("Arial",8,"bold"),fg="black")
# lb4.place(x=310,y=390)
"Entry"

ent=Entry(root,font=("Arial",17,"bold"),fg="black",borderwidth=5,textvariable=a)
ent.place(x=320,y=145)

ent1=Entry(root,font=("Arial",17,"bold"),fg="black",borderwidth=5,textvariable=b)
ent1.place(x=320,y=250)



#Buttons
bt=Button(root,text="GENERATE PASSWORD",font=("Arial",17,"bold"),fg="white",bg="blue",command=gen)
bt.place(x=350,y=420)

bt1=Button(root,text="Accept",font=("Arial",17,"bold"),fg="blue",command=acpt)
bt1.place(x=450,y=480)

bt2=Button(root,text="Reject",font=("Arial",17,"bold"),fg="blue",command=rjct)
bt2.place(x=450,y=540)

root.mainloop()