"""GUI tkinter application allowing user to enter a month and year from 1900 to 2200
and view the calendar for that period.
James Overholser
10/12/2021
"""

# importing modules
from tkinter import *
import calendar


# main window

root = Tk()
root.title("Calendar")
root.geometry("240x200")
root.resizable(0,0)



#define function for calendar display

def show():
    a = int(spin1.get())
    b = int(spin2.get())

    cal = calendar.month(b,a)  #pass year and month value

    txt.delete(0.0,END)
    txt.insert(INSERT,cal)
    


#label
lbl1 = Label(root,text="Month",font=('Helvetica',10,'bold')).place(x=15,y=0)

lbl2 = Label(root,text="Year",font=('Helvetica',10,'bold')).place(x=115,y=0)

#spinbox creation

spin1 = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
spin1.place(x=60,y=0)

spin2 = Spinbox(root,from_=1900,to= 2200,width=4)
spin2.place(x=150,y=0)

#button creation
btn = Button(root,text="Show",font=('Helvetica',10,'bold'),command=show).place(x=100,y=30)

#creation of textbox for calendar display

txt = Text(root,width=24,height=8)
txt.place(x=20,y=57)

root.mainloop()
           
                                    
