from tkinter import*
from tkinter import simpledialog
root=Tk()
root.geometry("1000x700+200+60")
root.resizable(1,1)
root.title("To-Do List")
root.config(bg="white smoke")

#functions
def add_item():
    item = a.get()
    if item:
        listbox.insert(END, item)
        a.set("")

        """delete button"""
        bt1=Button(root,font=("Arial",20),borderwidth="2",text="Delete",bg="black",fg="white",command=remove_item)
        bt1.place(x=710,y=260,width=100,height=50)

        """edit button"""
        bt2=Button(root,font=("Arial",20),borderwidth="2",text="Edit",bg="black",fg="white",command=edit_item)
        bt2.place(x=85,y=625,width=100,height=50)

def remove_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
def edit_item():
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = selected_index[0]
        old_item = listbox.get(selected_index)
        new_item = simpledialog.askstring("Edit Item", "Edit the item:", initialvalue=old_item)
        if new_item:
            listbox.delete(selected_index)
            listbox.insert(selected_index, new_item)

#entry
a=StringVar()
ent=Entry(root,font=("Arial",15),borderwidth="1",textvariable=a)
ent.place(x=80,y=260,width=500,height=50)

#Listbox
listbox=Listbox(root,font=("Arial",20),borderwidth="4")
listbox.place(x=80,y=320,width=700,height=300)

#label
lb=Label(root,font=("Arial",25),text="Add task:")
lb.place(x=80,y=210)

#buttons
bt=Button(root,font=("Arial",20),borderwidth="2",text="Add",bg="black",fg="white",command=add_item)
bt.place(x=600,y=260,width=100,height=50)

#canvas
can=Canvas(root,width="2000",height="200",bg="green2")
can.grid(row="0",column="0")
can.create_text("200","100",font=("Comic Sans MS",50),text="To Do list",fill="black")
root.mainloop()

