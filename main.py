from tkinter import *


root = Tk()
root.title("App")
root.geometry("470x200")

l1 = Label(root,text = "Lets calculate numbers")

b = Button(root,text = "Lets go!")
global k3
def clear():
    k3.destroy()

def checkop():


    if op.get() == '+':
        add()
    elif op.get() == '-':
        sub()
    elif op.get() == '*':
        mul()
    elif op.get() =='/':
        div()
    else:
        global k3
        k3 = Label(root,text = "invaid operator")
        k3.place(x = 50,y = 200)

def add():
    global k3
    k3 = Label(root, text ="Answer is " +  str(int(n1.get())+int(n2.get())))
    k3.place(x=50, y=200)

def sub():
    global k3
    k3 = Label(root, text ="Answer is " +  str(int(n1.get())-int(n2.get())))
    k3.place(x=50, y=200)


def mul():
    global k3
    k3 = Label(root, text ="Answer is " +  str(int(n1.get())*int(n2.get())))
    k3.place(x=50, y=200)

def div():
    global k3
    k3 = Label(root, text ="Answer is " +  str(int(n1.get())/int(n2.get())))
    k3.place(x=50, y=200)






l1.place(x = 200,y = 0)
b.place(x = 475,y = 20)

l2 = Label(root,text = "Enter n1: ")
l2.place(x = 10,y = 100)

n1 = Entry(root)
n1.place(x = 10, y = 130)


l2 = Label(root,text = "Enter n2: ")
l2.place(x = 150,y = 100)


n2 = Entry(root)
n2.place(x = 150, y = 130)

opl = Label(root,text = "Enter operator")
opl.place(x = 300,y = 100)
op = Entry(root)
op.place(x = 300,y = 130)


b2 = Button(root,text = "calculate",command = checkop)
b2.place(x = 60, y = 160)

cl = Button(root,text = "clear",command = clear)
cl.place(x = 150,y  = 160)


root.mainloop()