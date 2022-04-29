from tkinter import Toplevel, Button, Tk, Menu  
from tkinter import *
from scipy.stats import binom
import tkinter as tk 
import scipy.stats 
from scipy.stats import chi2
from scipy.stats import t

#Binomial Distribution
def bio():
    root = Tk()
    root.title("Binomial distribution Calculator")
    root.geometry("800x500")

    def val():
        if trial_entry.get() and prob_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Binomial distribution")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    trial_label = Label(my_frame,text = "How many trials (or subjects) per experiment?")
    trial_entry = Entry(my_frame,font=("Helvetica",18))

    prob_label = Label(my_frame,text = "What is the probability of 'success' in each trial or subject?")
    prob_entry = Entry(my_frame,font=("Helvetica",18))

    trial_label.grid(row=0,column=0)
    trial_entry.grid(row=0,column=1)
    prob_label.grid(row=1,column=0,pady=20)
    prob_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Compute Probability",command=val)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

#Gaussian Distribution
def gau():
    root = Tk()
    root.title("Gaussian distribution Calculator")
    root.geometry("500x500")

    def pval():
        if mean_entry.get() and sd_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Gaussian distribution")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    mean_label = Label(my_frame,text = "Mean")
    mean_entry = Entry(my_frame,font=("Helvetica",18))

    sd_label = Label(my_frame,text = "SD")
    sd_entry = Entry(my_frame,font=("Helvetica",18))

    mean_label.grid(row=0,column=0)
    mean_entry.grid(row=0,column=1)
    sd_label.grid(row=1,column=0,pady=20)
    sd_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Compute Probability",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)

    root.mainloop()

def poi():
    root = Tk()
    root.title("Poisson distribution Calculator")
    root.geometry("800x500")

    def pval():
        if o_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Poisson distribution")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    o_label = Label(my_frame,text = "Average number of objects per area (or events per unit time)?")
    o_entry = Entry(my_frame,font=("Helvetica",18))

    o_label.grid(row=0,column=0)
    o_entry.grid(row=0,column=1)

    my_button = Button(my_label_frame,text="Compute Probability",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def pft():
    root = Tk()
    root.title("P Value Calculator")
    root.geometry("500x500")

    def pval():
        if T_entry.get() and DF_entry.get():
            T = float(T_entry.get())
            DF = float(DF_entry.get())
            P = 2*(1 - t.cdf(abs(T), DF))
            P = f"{P:,.3f}"
            pval_label.config(text=f"P Value :- {P}")

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="P From T")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    T_label = Label(my_frame,text = "T Value")
    T_entry = Entry(my_frame,font=("Helvetica",18))

    DF_label = Label(my_frame,text = "DF Value")
    DF_entry = Entry(my_frame,font=("Helvetica",18))

    T_label.grid(row=0,column=0)
    T_entry.grid(row=0,column=1)
    DF_label.grid(row=1,column=0,pady=20)
    DF_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Calculate P Value",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def pfc():
    root = Tk()
    root.title("P Value Calculator")
    root.geometry("500x500")

    def pval():
        if chi_entry.get() and DF_entry.get():
            a = float(chi_entry.get())
            b = float(DF_entry.get())
            P = chi2.sf(a, b)
            P = f"{P:,.3f}"
            pval_label.config(text=f"P Value :- {P}")
        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="P From chi Square")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    chi_label = Label(my_frame,text = "chi Square Value")
    chi_entry = Entry(my_frame,font=("Helvetica",18))

    DF_label = Label(my_frame,text = "DF Value")
    DF_entry = Entry(my_frame,font=("Helvetica",18))

    chi_label.grid(row=0,column=0)
    chi_entry.grid(row=0,column=1)
    DF_label.grid(row=1,column=0,pady=20)
    DF_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Calculate P Value",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def pff():
    root = Tk()
    root.title("P Value Calculator")
    root.geometry("500x500")

    def pval():
        if F_entry.get() and DFn_entry.get() and DFd_entry.get():
            F = float(F_entry.get())
            DFn = float(DFn_entry.get())
            DFd = float(DFn_entry.get())
            P = 1-scipy.stats.f.cdf(F, DFn, DFd)
            P = f"{P:,.3f}"
            pval_label.config(text=f"P Value :- {P}")

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="P From F")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    F_label = Label(my_frame,text = "F Value")
    F_entry = Entry(my_frame,font=("Helvetica",18))

    DFn_label = Label(my_frame,text = "DFn Value")
    DFn_entry = Entry(my_frame,font=("Helvetica",18))

    DFd_label = Label(my_frame,text = "DFd Value")
    DFd_entry = Entry(my_frame,font=("Helvetica",18))

    F_label.grid(row=0,column=0)
    F_entry.grid(row=0,column=1)
    DFn_label.grid(row=1,column=0,pady=20)
    DFn_entry.grid(row=1,column=1)
    DFd_label.grid(row=2,column=0,pady=20)
    DFd_entry.grid(row=2,column=1)

    my_button = Button(my_label_frame,text="Calculate P Value",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def pfr():
    root = Tk()
    root.title("P Value Calculator")
    root.geometry("500x500")

    def pval():
        if r_entry.get() and DF_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="P From R")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    r_label = Label(my_frame,text = "r Value")
    r_entry = Entry(my_frame,font=("Helvetica",18))

    DF_label = Label(my_frame,text = "DF Value")
    DF_entry = Entry(my_frame,font=("Helvetica",18))

    r_label.grid(row=0,column=0)
    r_entry.grid(row=0,column=1)
    DF_label.grid(row=1,column=0,pady=20)
    DF_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Calculate P Value",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def pfz():
    root = Tk()
    root.title("P Value Calculator")
    root.geometry("500x500")

    def pval():
        if z_entry.get():
            z = float(z_entry.get())
            P = scipy.stats.norm.sf(abs(z))*2
            P = f"{P:,.3f}"
            pval_label.config(text=f"P Value :- {P}")

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="P From Z")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)

    z_label = Label(my_frame,text = "Z Value")
    z_entry = Entry(my_frame,font=("Helvetica",18))

    z_label.grid(row=0,column=0)
    z_entry.grid(row=0,column=1)

    my_button = Button(my_label_frame,text="Calculate P Value",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def chi():
    root = Tk()
    root.title("Chi Square Calculator")
    root.geometry("500x500")

    def pval():
        if prob_entry.get() and DF_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Chi Square")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    prob_label = Label(my_frame,text = "Probability")
    prob_entry = Entry(my_frame,font=("Helvetica",18))

    DF_label = Label(my_frame,text = "DF Value")
    DF_entry = Entry(my_frame,font=("Helvetica",18))

    prob_label.grid(row=0,column=0)
    prob_entry.grid(row=0,column=1)
    DF_label.grid(row=1,column=0,pady=20)
    DF_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Compute Chi-Square",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def fr():
    root = Tk()
    root.title("F Ratio Calculator")
    root.geometry("500x500")

    def pval():
        if prob_entry.get() and DFn_entry.get() and DFd_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="F Ratio")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    prob_label = Label(my_frame,text = "Probability")
    prob_entry = Entry(my_frame,font=("Helvetica",18))

    DFn_label = Label(my_frame,text = "DFn Value")
    DFn_entry = Entry(my_frame,font=("Helvetica",18))

    DFd_label = Label(my_frame,text = "DFd Value")
    DFd_entry = Entry(my_frame,font=("Helvetica",18))

    prob_label.grid(row=0,column=0)
    prob_entry.grid(row=0,column=1)
    DFn_label.grid(row=1,column=0,pady=20)
    DFn_entry.grid(row=1,column=1)
    DFd_label.grid(row=2,column=0,pady=20)
    DFd_entry.grid(row=2,column=1)

    my_button = Button(my_label_frame,text="Compute F",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def tr():
    root = Tk()
    root.title("T Ratio Calculator")
    root.geometry("500x500")

    def pval():
        if prob_entry.get() and DF_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="T Ratio")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    prob_label = Label(my_frame,text = "Probability")
    prob_entry = Entry(my_frame,font=("Helvetica",18))

    DF_label = Label(my_frame,text = "DF Value")
    DF_entry = Entry(my_frame,font=("Helvetica",18))

    prob_label.grid(row=0,column=0)
    prob_entry.grid(row=0,column=1)
    DF_label.grid(row=1,column=0,pady=20)
    DF_entry.grid(row=1,column=1)

    my_button = Button(my_label_frame,text="Compute T",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def zr():
    root = Tk()
    root.title("Z Ratio Calculator")
    root.geometry("500x500")

    def pval():
        if prob_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Z Ratio")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    prob_label = Label(my_frame,text = "Probability")
    prob_entry = Entry(my_frame,font=("Helvetica",18))


    prob_label.grid(row=0,column=0)
    prob_entry.grid(row=0,column=1)

    my_button = Button(my_label_frame,text="Compute Z",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()

def cptp():
    root = Tk()
    root.title("Interpret P values")
    root.geometry("500x500")

    def pval():
        if alpha_entry.get() and power_entry.get() and prob_entry.get():
            pass

        else:
            pval_label.config(text="Hey! You Forgot To Enter Something.....")

    my_label_frame = LabelFrame(root,text="Compute post test probability")
    my_label_frame.pack(pady=30)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=20,padx=20)


    alpha_label = Label(my_frame,text = "Alpha:")
    alpha_entry = Entry(my_frame,font=("Helvetica",18))

    power_label = Label(my_frame,text = "Power (%):")
    power_entry = Entry(my_frame,font=("Helvetica",18))

    prob_label = Label(my_frame,text = "Prior probability (%)")
    prob_entry = Entry(my_frame,font=("Helvetica",18))

    alpha_label.grid(row=0,column=0)
    alpha_entry.grid(row=0,column=1)
    power_label.grid(row=1,column=0,pady=20)
    power_entry.grid(row=1,column=1)
    prob_label.grid(row=2,column=0,pady=20)
    prob_entry.grid(row=2,column=1)

    my_button = Button(my_label_frame,text="Compute",command=pval)
    my_button.pack(pady=20)

    pval_label = Label(root,text="",font=("helvetica",18))
    pval_label.pack(pady=20)
    root.mainloop()



root = Tk()  
root.title("Calulator for probability values for different distribution")
menubar = Menu(root) 
root.geometry("600x500")


file = Menu(menubar, tearoff=0)  
file.add_command(label="P form t",command = pft)  
file.add_command(label="P from chi",command = pfc)  
file.add_command(label="P from f",command = pff)  
file.add_command(label="P form r",command = pfr)  
file.add_command(label="P from z",command = pfz)  
    
menubar.add_cascade(label="Calulate P", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Binomial Distrubtion",command = bio)
edit.add_command(label="Gaussian Distrubtion",command = gau)
edit.add_command(label="Poisson Distrubtion",command = poi)
  
menubar.add_cascade(label="Distribution", menu=edit)  

help = Menu(menubar, tearoff=0)  
help.add_command(label="Chi",command = chi)
help.add_command(label="F Ratio",command = fr)
help.add_command(label="T Ratio",command = tr)
help.add_command(label="Z Ratio",command = zr)
menubar.add_cascade(label="From Probability", menu=help) 

help = Menu(menubar, tearoff=0)  
help.add_command(label="F Test")
menubar.add_cascade(label="Compare", menu=help)

help = Menu(menubar, tearoff=0)  
help.add_command(label="Compute Post Test Probablility",command = cptp)
help.add_command(label="Multiple Comparisons Correction")
menubar.add_cascade(label="Interpet P Value", menu=help)  
  
root.config(menu=menubar)  
title_label = Label(text = 'Calculator for Probability values for different Distribution', font=('Arial',16))
title_label.pack()
author_label = Label(text = 'Author Details: Mohit , Isha and Deven ',font=('Arial',12) )
author_label.pack()

quitButton = Button(text = 'Quit from System', command=root.destroy,bg = '#ffffff',activebackground = 'blue').pack(padx=5, pady=20, side=tk.BOTTOM)
root.mainloop()
