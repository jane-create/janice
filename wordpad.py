from tkinter import *

top = Tk()
top.geometry('500x500')
top.title('Untitled - Notepad')



l1 =Label(top, text ='URL')
l2 =Label(top, text ='VERSION NUMBER')
l3 =Label(top, text ='DIFF NUMBER')
l4 =Label(top, text ='View')
l5 =Label(top, text = 'Help')
l1.grid(row =0, column =1)
l2.grid(row =0, column =2)
l3.grid(row =0, column =3)
l4.grid(row =0, column =4)
l5.grid(row =0, column =5)





top.mainloop()

