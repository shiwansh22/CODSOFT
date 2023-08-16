from tkinter import*
import math
root=Tk()
root.geometry("330x400+50+80")
root.resizable(1,1)
root.title("Calculator")
root.config(bg="grey90")
def show(op):
    x=a.set(a.get()+op)
def eql():
    exp=a.get()
    a.set(eval(exp))
def clr():
    a.set(" ")
def rot():
    r=float(a.get())
    a.set(math.sqrt(r))
def fact():
    fac=int(a.get())
    a.set(math.factorial(fac))
def per():
    ln=int(a.get())/100
    a.set(str(ln))
    
a = StringVar()
ent = Entry(root,borderwidth="3" ,justify = "right",font = ("Arial",15),textvariable = a)
ent.place(x=10 , y=15, width = 300, height = 40)

bc = Button(root,borderwidth="3" , text = "C",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bc.place(x=20, y=65 ,width = 40, height = 50 )
bc.configure(command = lambda:clr())

b7 = Button(root,borderwidth="3" , text = "7",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b7.place(x=20, y=125 ,width = 40, height = 50 )
b7.configure(command = lambda:show("7"))

b4 = Button(root,borderwidth="3" , text = "4",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b4.place(x=20, y=185 ,width = 40, height = 50 )
b4.configure(command = lambda:show("4"))

b1 = Button(root,borderwidth="3" ,text = "1",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b1.place(x=20, y=245 ,width = 40, height = 50 )
b1.configure(command = lambda:show("1"))

bfa = Button(root,borderwidth="3" , text = "!",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bfa.place(x=20, y=305 ,width = 40, height = 50 )
bfa.configure(command = lambda:fact())

bsqrt = Button(root,borderwidth="3" , text = "√",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bsqrt.place(x=100, y=65 ,width = 40, height = 50 )
bsqrt.configure(command = lambda:rot())

b8 = Button(root,borderwidth="3" , text = "8",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b8.place(x=100, y=125 ,width = 40, height = 50 )
b8.configure(command = lambda:show("8"))

b5 = Button(root,borderwidth="3" , text = "5",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b5.place(x=100, y=185 ,width = 40, height = 50 )
b5.configure(command = lambda:show("5"))

b2 = Button(root,borderwidth="3" , text = "2",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b2.place(x=100, y=245 ,width = 40, height = 50 )
b2.configure(command = lambda:show("2"))

b0 = Button(root,borderwidth="3" , text = "0",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b0.place(x=100, y=305 ,width = 40, height = 50 )
b0.configure(command = lambda:show("0"))

bd = Button(root,borderwidth="3" , text = "/",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bd.place(x=180, y=65 ,width = 40, height = 50 )
bd.configure(command = lambda:show("/"))

b9 = Button(root,borderwidth="3" , text = "9",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b9.place(x=180, y=125 ,width = 40, height = 50 )
b9.configure(command = lambda:show("9"))

b6 = Button(root,borderwidth="3" , text = "6",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b6.place(x=180, y=185 ,width = 40, height = 50 )
b6.configure(command = lambda:show("6"))

b3 = Button(root, borderwidth="3" ,text = "3",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
b3.place(x=180, y=245 ,width = 40, height = 50 )
b3.configure(command = lambda:show("3"))

bdot = Button(root,borderwidth="3" , text = ".",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bdot.place(x=180, y=305 ,width = 40, height = 50 )
bdot.configure(command = lambda:show("."))

bgeq = Button(root,borderwidth="3" , text = "%",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bgeq.place(x=260, y=65 ,width = 40, height = 50 )
bgeq.configure(command = lambda:per())

bm = Button(root, borderwidth="3" ,text = "*",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bm.place(x=260, y=125 ,width = 40, height = 50 )
bm.configure(command = lambda:show("*"))

bs = Button(root,borderwidth="3" ,text = "-",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
bs.place(x=260, y=185 ,width = 40, height = 50 )
bs.configure(command = lambda:show("-"))

ba = Button(root,borderwidth="3" , text = "+",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
ba.place(x=260, y=245 ,width = 40, height = 50 )
ba.configure(command = lambda:show("+"))

beq = Button(root,borderwidth="3" , text = "=",justify = "right", font = ("Arial",15),fg ="black",bg="gray90")
beq.place(x=260, y=305 ,width = 40, height = 50 )
beq.configure(command = lambda:eql())

root.mainloop()