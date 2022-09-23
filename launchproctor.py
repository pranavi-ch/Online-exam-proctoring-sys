#Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import multiTask
#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of Tkinter Frame
win.geometry("700x350")

#Define a function for opening the Dialog box
def open_proctor():
  # multiTask.openForm()
  win.destroy()
  import multiTask
  

#Create a Label widget
Label(win, text= "Start Exam!").pack(pady=15)

#Create a Button for opening a dialog Box
ttk.Button(win, text= "Open Test", command= open_proctor).pack()

win.mainloop()