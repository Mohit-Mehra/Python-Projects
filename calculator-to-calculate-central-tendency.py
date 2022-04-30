from os import read
from tkinter import *
import tkinter as tk 
from tkinter import ttk
import tkinter.messagebox as tmsg
import numpy as np
import statistics



root = Tk() 
root.title("Project-1: Measure of Central Tendency and Dispersion")
root.minsize(500, 500) 
root.maxsize(1200, 988)


title_label = Label(text = 'Title: Measure of Central Tendancy and Dispersion', font=('Arial',16))
author_label = Label(text = 'Author Details: Mohit Mehra',font=('Arial',12) )
title_label.pack()
author_label.pack()

number_label = Label(text = 'Enter List of Numbers: ',font=('Arial',10) ).place(x=10, y=75)
number_text = Entry(root)
number_text.place(x=180, y=75)

def Arithmetic():  
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    m = statistics.mean(a)
    tmsg.showinfo("Arithmetic mean ", m)

def harmonicmean():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    h = statistics.harmonic_mean(a)
    tmsg.showinfo("Harmonic mean", h)

def geometricmean():  
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    g = statistics.geometric_mean(a)
    tmsg.showinfo("Geometricmean mean ", g)

def mode():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    m = statistics.mode(a)
    tmsg.showinfo("Mode ", m)

def median():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    m = statistics.median(a)
    tmsg.showinfo("Median", m)

def Range():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    r = max(a) - min(a)
    tmsg.showinfo("Range",r)

def Variance():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    v = statistics.variance(a)
    tmsg.showinfo("Variance",v)


def Standard_Deviation():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    v = np.std(a)
    tmsg.showinfo("Standard_Deviation",v)

def Quartile_Deviation():
    values = number_text.get().split(',')
    array = np.array(values)
    a = array.astype(int)
    Q1 = np.quantile(a, 0.25)
    Q2 = np.quantile(a, 0.50)
    Q3 = np.quantile(a, 0.75)
    q = (Q3 - Q1)/2
    tmsg.showinfo("Standard_Deviation",q)

ctLabel = Label(text = 'Measure of Central Tendancy',font=('Arial',12) ).place(x=10, y=150)
var = IntVar()
r1_ct = Radiobutton(text = "Airthmetic Mean", variable = var, value = 1,command = Arithmetic).place(x=10, y=200)
r2_ct = Radiobutton(text = "Harmonic Mean", variable = var, value = 2,command = harmonicmean).place(x=10, y=220)
r3_ct = Radiobutton(text = "Geometric Mean", variable = var, value = 3,command = geometricmean).place(x=10, y=240)
r4_ct = Radiobutton(text = "Mode", variable = var, value = 4,command = mode).place(x=10, y=260)
r5_ct = Radiobutton(text = "Median", variable = var, value = 5,command = median).place(x=10, y=280)
 
dispLabel = Label(text = 'Measure of Dispersion',font=('Arial',12) ).place(x=10, y=310)
var1 = IntVar()
r1_c = Radiobutton(text = "Range", variable = var1, value = 6,command = Range).place(x=10, y=360)
r2_c = Radiobutton(text = "Variance", variable = var1, value = 7,command = Variance).place(x=10, y=380)
r3_c = Radiobutton(text = "Standard_Deviation", variable = var1, value = 8,command = Standard_Deviation).place(x=10, y=400)
r4_c = Radiobutton(text = "Quartile", variable = var1, value = 9,command = Quartile_Deviation).place(x=10, y=420)


quitButton = Button(text = 'Quit from System', command=root.destroy).pack(padx=5, pady=20, side=tk.BOTTOM)

root.mainloop()


 
  
 
  

  

        