import tkinter as tk
from tkinter.constants import BOTH, BOTTOM, E, EW, LEFT, N, NSEW, RIGHT, TOP, W
from PIL import ImageTk, Image
import os

def btn_forward():
    global file_names
    global my_image_window
    global my_image_frame
    global size
    global my_image
    global index
   
    if index == len(file_names) - 1:
        index = -1

    my_image_frame.pack_forget()
    my_image_window.pack_forget()
    btn_frame.pack_forget()
    btn_exit_frame.pack_forget()
    bottom_frame.pack_forget()

    tmp_image = Image.open('images/'+file_names[index + 1])
    tmp_image.thumbnail(size, Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(tmp_image)

    my_image_frame = tk.Frame(window, width = 1000, height = 1000)
    my_image_frame.pack()

    my_image_window = tk.Label(my_image_frame, image = my_image)
    my_image_window.pack()

    index += 1
 
    reDraw()

def btn_backward():
    global file_names
    global my_image_window
    global my_image_frame
    global size
    global my_image
    global index
   
    if index == 0:
        index = len(file_names)

    my_image_frame.pack_forget()
    my_image_window.pack_forget()
    btn_frame.pack_forget()
    btn_exit_frame.pack_forget()
    bottom_frame.pack_forget()

    tmp_image = Image.open('images/'+file_names[index - 1])
    tmp_image.thumbnail(size, Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(tmp_image)

    my_image_frame = tk.Frame(window, width = 1000, height = 1000)
    my_image_frame.pack()

    my_image_window = tk.Label(my_image_frame, image = my_image)
    my_image_window.pack()

    index -= 1

    reDraw()

def reDraw():
    global btn_frame
    global btn_exit_frame
    global btn_bk
    global btn_fwd
    global btn_space1
    global btn_space2
    global btn_exit
    global bottom_frame

    bottom_frame = tk.Frame(window)
    bottom_frame.pack(side = BOTTOM)

    btn_frame = tk.Frame(bottom_frame)
    btn_frame.pack(side = LEFT)

    btn_exit_frame = tk.Frame(bottom_frame)
    btn_exit_frame.pack(side = RIGHT)

    btn_bk = tk.Button(btn_frame, text = '<', command = btn_backward)
    btn_fwd = tk.Button(btn_frame, text = '>', command = btn_forward)
    btn_space1 = tk.LabelFrame(btn_frame, width = 480)
    btn_space2 = tk.LabelFrame(btn_frame, width = 350)
    btn_exit = tk.Button(btn_exit_frame, text = 'Exit', command = window.quit)

    btn_space1.grid(row = 1, column = 0)
    btn_bk.grid(row = 1, column = 1)
    btn_fwd.grid(row = 1, column = 2)
    btn_space2.grid(row = 1, column = 3)
    btn_exit.grid(row = 0, column = 0, sticky = E)

index = 0
file_names = os.listdir('images')
size = 1000, 1000

window = tk.Tk()
window.title("Some Program")
window.geometry('1000x1100')
window.minsize(1000, 1100)

tmp_image = Image.open('images/'+file_names[index])
tmp_image.thumbnail(size, Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(tmp_image)

my_image_frame = tk.Frame(window, width = 1000, height = 1000)
my_image_frame.pack(side = TOP)

my_image_window = tk.Label(my_image_frame, image = my_image)
my_image_window.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side = BOTTOM)

btn_frame = tk.Frame(bottom_frame)
btn_frame.pack(side = LEFT)

btn_exit_frame = tk.Frame(bottom_frame)
btn_exit_frame.pack(side = RIGHT)

btn_bk = tk.Button(btn_frame, text = '<', command = btn_backward)
btn_fwd = tk.Button(btn_frame, text = '>', command = btn_forward)
btn_space1 = tk.LabelFrame(btn_frame, width = 480)
btn_space2 = tk.LabelFrame(btn_frame, width = 350)
btn_exit = tk.Button(btn_exit_frame, text = 'Exit', command = window.quit)

btn_space1.grid(row = 1, column = 0)
btn_bk.grid(row = 1, column = 1)
btn_fwd.grid(row = 1, column = 2)
btn_space2.grid(row = 1, column = 3)
btn_exit.grid(row = 0, column = 0)

window.mainloop()