from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
from tkinter import ttk
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
#######
#  Title: Correlation Analysis.
# 
# @author Dr. Rajeev Gupta
# co-author: Mohit Mehra & Isha
# 
# @version 1.00	22.11.2021 -  Baseline Code
# version: 1.1   15.12.2021 - updated code
########


## browse function will open the file section for selecting the excel sheet and we also search it into
#  taskbar in search option  through sheet name.
def browse():
    global loc
    loc = fd.askopenfilename()
    lab_3 = Label(root, text = loc)
    lab_3.place(x=300, y=45)

    ## loaddata will open the excel table in the GUI to easily check the data. if other than .elsv file selected 
    ## it will sow error message.
def loaddata():    
        if loc:
            try:
                filename = r"{}".format(loc)
                df = pd.read_excel(filename)
            except ValueError:
                my_label.config(text="File Couldn't Open")
            except FileNotFoundError:
                my_label.config(text="File Couldn't found")

        clear_tree() 
## it is covering the area of excel table in loaddata.
        my_tree["column"] = list(df.columns)
        my_tree['show'] = "headings"

        for column in my_tree["column"]:
            my_tree.heading(column,text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("","end",values=row)

        my_tree.pack()

## it will clear the excel table on screen
def clear_tree():
    my_tree.delete(*my_tree.get_children())

## Karl Pearson's coefficient of correlation is defined as a linear 
# correlation coefficient that falls in the value range of -1 to +1. Value of -1 
# signifies strong negative correlation while +1 indicates strong positive correlation.
def kp():
    filename = r"{}".format(loc)
    df = pd.read_excel(filename)
    kp = df.corr(method='pearson')
    print(kp)
    clear_tree()
    my_tree["column"] = list(kp.columns)
    my_tree['show'] = "headings"

    for column in my_tree["column"]:
        my_tree.heading(column,text=column)

    df_rows = kp.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("","end",values=row)

    my_tree.pack()

  ## a rank correlation is any of several statistics that measure an ordinal association
def rankcor():
    filename = r"{}".format(loc)
    df = pd.read_excel(filename)
    rankcor = df.corr(method='spearman')
    print(kp)
    clear_tree()
    my_tree["column"] = list(rankcor.columns)
    my_tree['show'] = "headings"

    for column in my_tree["column"]:
        my_tree.heading(column,text=column)

    df_rows = rankcor.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("","end",values=row)

    my_tree.pack()

## data visualization will show the graphical representation of the above searched table that retrived
## from load data
def datavis():
    filename = r"{}".format(loc)
    df = pd.read_excel(filename)
    a = df['Roll No']
    b = df["Marks"]
    plt.plot(a,b)
    plt.show()

## creating the main window
root = Tk()
root.title("GUI APP - Correlation in Python")
root.geometry('800x800')
root.minsize(800,600)

l1 = Label(root,text = "Correlation Project",font=('Arial',16))
l1.place(x=340,y=5)
l2 = Label(root,text = "Selected Data", font=('Arial',16))
l2.place(x=10,y=45)

## creating a browse button 
browsebutton = Button(root,text="Browse",command=browse)
browsebutton.place(x=650,y=45,width=100)

##creating a  loadbutton 
loadbutton = Button(root,text = "Load Data",command=loaddata)
loadbutton.place(x=650,y=85,width=100)

## creating a karlpearson button
kpcorbutton = Button(root,text = "Karl Pearson",command=kp)
kpcorbutton.place(x=650,y=125,width=100)

#### creating a rankcorrelation button
rankcorbutton = Button(root,text="Rank Correlation",command=rankcor)
rankcorbutton.place(x=650,y=165,width=100)

## creating a datavisualization button
datavisbutton = Button(root,text = "Data Visualization",command=datavis)
datavisbutton.place(x=650,y=205,width=100)

## Quit button will destroy the output screen
quitbutton = Button(root,text = "Quit from System",command=root.destroy)
quitbutton.place(x=650,y=250,width=100)

my_frame = Frame(root)
my_frame.place(x=30,y=100)

my_tree = ttk.Treeview( my_frame)

my_label = Label(root,text='')
my_label.place(x =30,y=500)
root.mainloop()