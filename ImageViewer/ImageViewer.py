import tkinter as tk
from tkinter.constants import E, N, W
from PIL import ImageTk, Image
import os

def btn_forward():
    global file_names
    global my_image_window
    global size
    global my_image
    global index

    if index == len(file_names) - 1:
        index = -1

    my_image_window.grid_forget()
    
    tmp_image = Image.open('images/'+file_names[index + 1])
    tmp_image.thumbnail(size, Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(tmp_image)
    my_image_window = tk.Label(image = my_image, anchor = N)
    my_image_window.grid(row = 0, column = 0, columnspan = 6)

    index += 1
 

def btn_backward():
    global file_names
    global my_image_window
    global size
    global my_image
    global index

    if index == 0:
        index = len(file_names)

    my_image_window.grid_forget()
    
    tmp_image = Image.open('images/'+file_names[index - 1])
    tmp_image.thumbnail(size, Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(tmp_image)
    my_image_window = tk.Label(image = my_image, anchor = N)
    my_image_window.grid(row = 0, column = 0, columnspan = 6)

    index -= 1

index = 0
file_names = os.listdir('images')
size = 1000, 1000

window = tk.Tk()
window.title("Some Program")

tmp_image = Image.open('images/'+file_names[index])
tmp_image.thumbnail(size, Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(tmp_image)

my_image_window = tk.Label(image = my_image, anchor = N)
my_image_window.grid(row = 0, column = 0, columnspan = 6)

btn_bk = tk.Button(window, text = '<', command = btn_backward)
btn_fwd = tk.Button(window, text = '>', command = btn_forward)
btn_exit = tk.Button(window, text = 'Exit', command = window.quit)

btn_bk.grid(row = 1, column = 2, sticky = E)
btn_fwd.grid(row = 1, column = 3, sticky = W)
btn_exit.grid(row = 1, column = 5, sticky = E)

window.mainloop()