import tkinter as tk
from tkinter.constants import END
import math

def parse(calc):
    while '(' in calc and ')' in calc:
        start = findLastOpenParen(calc)
        end = findFirstCloseParen(calc)
        tmp = calc[start:end + 1]
        for i in range(len(tmp) - 1):
            del calc[start + 1]
        calc[start] = calculate(tmp)
    
    calculate(calc)

def findLastOpenParen(calc):
    return len(calc) - calc[-1::-1].index('(') - 1

def findFirstCloseParen(calc):
    return calc.index(')')

def calculate(calc):
    if('(' in calc and ')' in calc):
        calc.remove('(')
        calc.remove(')')

    operatorIndex = 0

    while 'sqr' in calc:
        operatorIndex = calc.index('sqr')
        calc[operatorIndex - 1] = str(float(calc[operatorIndex -1]) * float(calc[operatorIndex -1]))
        del calc[operatorIndex]

    while 'sqrt' in calc:
        operatorIndex = calc.index('sqrt')
        calc[operatorIndex - 1] = str(math.sqrt(float(calc[operatorIndex -1])))
        del calc[operatorIndex]

    while '*' in calc:
        operatorIndex = calc.index('*')
        calc[operatorIndex - 1] = str(float(calc[operatorIndex - 1]) * float(calc[operatorIndex + 1]))
        del calc[operatorIndex]
        del calc[operatorIndex]

    while '/' in calc:
        operatorIndex = calc.index('/')
        calc[operatorIndex - 1] = str(float(calc[operatorIndex - 1]) / float(calc[operatorIndex + 1]))
        del calc[operatorIndex]
        del calc[operatorIndex]

    while '+' in calc:
        operatorIndex = calc.index('+')
        calc[operatorIndex - 1] = str(float(calc[operatorIndex - 1]) + float(calc[operatorIndex + 1]))
        del calc[operatorIndex]
        del calc[operatorIndex]

    while '-' in calc:
        operatorIndex = calc.index('-')
        calc[operatorIndex - 1] = str(float(calc[operatorIndex - 1]) - float(calc[operatorIndex + 1]))
        del calc[operatorIndex]
        del calc[operatorIndex]

    return str(calc[0])

f_num = 0.0
operator = ""
calc = []
numUndos = 50
undo = [""] * numUndos

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    calc.append(number)
    line = str(current) + str(number)
    entry.insert(0, line)
    global undo

    if len(undo) <= numUndos:
        undo.append(line)
    else:
        del undo[0]
        undo.append(line)

def button_add():
    global operator
    operator = "+"
    button_click(operator)
    
def button_mod():
    global operator
    operator = "%"
    button_click(operator)

def button_div():
    global operator
    operator = "/"
    button_click(operator)

def button_mult():
    global operator
    operator = "*"
    button_click(operator)

def button_min():
    global operator
    operator = "-"
    button_click(operator)

def button_sqr():
    global operator
    operator = "sqr"
    button_click(operator)

def button_sqrt():
    global operator
    operator = "sqrt"
    button_click(operator)

def button_undo():
    global undo
    global calc
    entry.delete(0, tk.END)
    del undo[len(undo) - 1]
    entry.insert(0, undo[len(undo) - 1])
    current = entry.get()
    calc.clear()
    for elem in current:
        calc.append(elem)

def button_equal():
    current = entry.get()
    parse(calc)
    display.insert(tk.END, "\n" + current + " = " + calc[0])
    display.see("end")
    entry.delete(0, tk.END)
    entry.insert(0, calc[0])
    current = entry.get()
    global undo
    undo.append(current)

def button_clear():
    entry.delete(0, tk.END)
    calc.clear()


#define windows
window = tk.Tk()
window.title("Simple Calculator")

display = tk.Text(master = window, height = 5, width = 35, borderwidth = 1)
display.grid(row = 0, column = 0, rowspan = 2, columnspan = 6, sticky = 'new')

entry = tk.Entry(master = window, width = 35, borderwidth = 5)
entry.grid(row = 3, column = 0, columnspan = 6, padx = 10, pady = 10, sticky = 'new')
entry.grid_rowconfigure(1, weight = 1)
entry.grid_columnconfigure(0, weight = 1)

# Define buttons
btn_1 = tk.Button(master = window, text= "1", padx = 20, pady = 10, command = lambda: button_click(1))
btn_2 = tk.Button(master = window, text= "2", padx = 20, pady = 10, command = lambda: button_click(2)) 
btn_3 = tk.Button(master = window, text= "3", padx = 20, pady = 10, command = lambda: button_click(3)) 
btn_4 = tk.Button(master = window, text= "4", padx = 20, pady = 10, command = lambda: button_click(4)) 
btn_5 = tk.Button(master = window, text= "5", padx = 20, pady = 10, command = lambda: button_click(5)) 
btn_6 = tk.Button(master = window, text= "6", padx = 20, pady = 10, command = lambda: button_click(6)) 
btn_7 = tk.Button(master = window, text= "7", padx = 20, pady = 10, command = lambda: button_click(7)) 
btn_8 = tk.Button(master = window, text= "8", padx = 20, pady = 10, command = lambda: button_click(8)) 
btn_9 = tk.Button(master = window, text= "9", padx = 20, pady = 10, command = lambda: button_click(9)) 
btn_0 = tk.Button(master = window, text= "0", padx = 20, pady = 10, command = lambda: button_click(0))
btn_dot = tk.Button(master = window, text= ".", padx = 20, pady = 10, command = lambda: button_click('.'))
btn_open_par = tk.Button(master = window, text= "(", padx = 20, pady = 10, command = lambda: button_click('('))
btn_close_par = tk.Button(master = window, text= ")", padx = 20, pady = 10, command = lambda: button_click(')'))
btn_mod = tk.Button(master = window, text= "%", padx = 20, pady = 10, command = button_mod)
btn_div = tk.Button(master = window, text= "/", padx = 20, pady = 10, command = button_div)
btn_mult = tk.Button(master = window, text= "*", padx = 20, pady = 10, command = button_mult)
btn_min = tk.Button(master = window, text= "-", padx = 20, pady = 10, command = button_min)
btn_add = tk.Button(master = window, text= "+", padx = 20, pady = 10, command = button_add)
btn_undo = tk.Button(master = window, text= "<-", padx = 20, pady = 10, command = button_undo) 
btn_sqr = tk.Button(master = window, text= "sqr", padx = 20, pady = 10, command = button_sqr)
btn_sqrt = tk.Button(master = window, text= "sqrt", padx = 20, pady = 10, command = button_sqrt)

btn_clear = tk.Button(master = window, text= "C", padx = 20, pady = 10, command = button_clear) 
btn_equal = tk.Button(master = window, text= "=", padx = 20, pady = 10, command = button_equal) 

# Put the buttons on the screen
btn_7.grid(row = 4, column = 0, sticky = 'nsew')
btn_8.grid(row = 4, column = 1, sticky = 'nsew')
btn_9.grid(row = 4, column = 2, sticky = 'nsew')
btn_div.grid(row = 4, column = 3, sticky = 'nsew')
btn_undo.grid(row = 4, column = 4, sticky = 'nsew')
btn_clear.grid(row = 4, column = 5, sticky = 'nsew')

btn_4.grid(row = 5, column = 0, sticky = 'nsew')
btn_5.grid(row = 5, column = 1, sticky = 'nsew')
btn_6.grid(row = 5, column = 2, sticky = 'nsew')
btn_mult.grid(row = 5, column = 3, sticky = 'nsew')
btn_open_par.grid(row = 5, column = 4, sticky = 'nsew')
btn_close_par.grid(row = 5, column = 5, sticky = 'nsew')

btn_1.grid(row = 6, column = 0, sticky = 'nsew')
btn_2.grid(row = 6, column = 1, sticky = 'nsew')
btn_3.grid(row = 6, column = 2, sticky = 'nsew')
btn_min.grid(row = 6, column = 3, sticky = 'nsew')
btn_sqr.grid(row = 6, column = 4, sticky = 'nsew')
btn_sqrt.grid(row = 6, column = 5, sticky = 'nsew')

btn_0.grid(row = 7, column = 0, sticky = 'nsew')
btn_dot.grid(row = 7, column = 1, sticky = 'nsew')
btn_mod.grid(row = 7, column = 2, sticky = 'nsew')
btn_add.grid(row = 7, column = 3, sticky = 'nsew')
btn_equal.grid(row = 7, column = 4, columnspan = 2, sticky = 'nsew')

# main loop is applied at the end of the file
window.mainloop()