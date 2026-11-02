from tkinter import *
import tkinter as tk

import math

window = Tk()
window.title("Calculator")
window.geometry("500x500")

user_input =Entry(window, width=50, bg="white", fg="black", borderwidth=3, relief="groove")
user_input.place(x=0,y=0)

def click(num):
    result = user_input.get()
    user_input.delete(0,END)
    user_input.insert(0,str(result) + str(num))

buttons =tk.Button(window, text ="1", width = 14, command= lambda: click(1))
buttons.place(x = 20, y = 70)
buttons =tk.Button(window, text ="2", width = 14, command= lambda: click(2))
buttons.place(x = 90, y = 70)
buttons =tk.Button(window, text ="3", width = 14, command= lambda: click(3))
buttons.place(x =180, y = 70)
buttons =tk.Button(window, text ="4", width = 14, command= lambda: click(4))
buttons.place(x =20, y = 120)
buttons =tk.Button(window, text ="5", width = 14, command= lambda: click(5))
buttons.place(x =90, y = 120)
buttons =tk.Button(window, text ="6", width = 14, command= lambda: click(6))
buttons.place(x =180, y = 120)
buttons =tk.Button(window, text ="7", width = 14, command= lambda: click(7))
buttons.place(x =20, y = 180)
buttons =tk.Button(window, text ="8", width = 14, command= lambda: click(8))
buttons.place(x =90, y = 180)
buttons =tk.Button(window, text ="9", width = 14, command= lambda: click(9))
buttons.place(x =180, y = 180)
buttons =tk.Button(window, text ="0", width = 14, command= lambda: click(0))
buttons.place(x =20, y = 240)

def add():
    n1 = user_input.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    user_input.delete(0,END)
buttons =tk.Button(window, text ="+", width = 14, command= add)
buttons.place(x =90 , y = 240)

def sub():
    n1 = user_input.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    user_input.delete(0,END)
buttons =tk.Button(window, text ="-", width = 14, command= sub)
buttons.place(x =180 , y = 240)

def multiply():
    n1 = user_input.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    user_input.delete(0,END)
buttons =tk.Button(window, text ="*", width = 14, command= multiply)
buttons.place(x =20 , y = 300)

def divide():
    n1 = user_input.get()
    global math
    math = "division"
    global i
    i = int(n1)
    user_input.delete(0,END)
buttons =tk.Button(window, text ="/", width = 14, command= divide)
buttons.place(x =90 , y = 300)

def equals():
    n2 = user_input.get()
    user_input.delete(0,END)
    if math =="addition":
        user_input.insert(0,i + int(n2))
    elif math =="subtraction":
        user_input.insert(0,i - int(n2))
    elif math =="multiplication":
        user_input.insert(0,i * int(n2))
    elif math =="division":
        user_input.insert(0,i / int(n2))

buttons =tk.Button(window, text ="=", width = 14, command= equals )
buttons.place(x =180 , y = 300)

def clear():
    user_input.delete(0,END)
buttons =tk.Button(window, text ="clear", width = 14, command= clear)
buttons.place(x =100 , y = 360)

window.mainloop()