# * means to import everything from the library
from tkinter import *

root = Tk()
# Adding a title to the program so that it display on the top bar of the window
root.title("My 1st Program")

# Label() is like a widget
#myLabel1 = Label(root, text = "I am Liu")
#myLabel2 = Label(root, text = "I have a turtle")

# positions myLabel1 in row 0 col 0. If you use the grid you don't need to pack.
#myLabel1.grid(row = 0, column = 0)
#myLabel2.grid(row = 1, column = 0)

# pack function puts text inside the window. If you pack you don't need to use grid.
#myLabel1.pack()

def myClick():
    myLabel1 = Label(root, text = "Hello " + e.get())
    myLabel1.pack()

# Creating an entry field on top of button. Changing width of the box using width = 50, height = 10
e = Entry(root, width = 50)
e.pack()
# Inserting text inside the field, first number is the index of the field
e.insert(0, "Enter your name: ")

#better way of coding this
#myLabel1 = Label(root, text = "I am Liu").grid(row = 0, column = 0)
#myLabel2 = Label(root, text = "I have a turtle").grid(row = 1, column = 0)

#buttons, buttons are enabled by default, add state = DISABLED to disable it (grey it out)
#padx = 200, pady = 100 makes the button bigger. Leaving out padx will just make the button as long as the text
#adding functionality to a button, add command = myClick to the button to add the function to it. 
#If we add () after myClick the functon automatically runs and we can't click on it
#Making the font blue using fg = 'blue'
#Making background color red bg = 'red'
# Inputting a name using e.get() in the myClick function to display name as a label
myButton = Button(root, text = "Enter your name", pady = 25, command = myClick, fg = 'blue', bg = 'red')
myButton.pack()





root.mainloop()
