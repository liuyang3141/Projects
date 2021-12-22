import tkinter as tk
from tkinter.constants import END
import math

def parse(calc):
    while '(' in calc and ')' in calc:
        start = findLastOccurence(calc, '(')
        end = findFirstOccurence(calc, ')')
        tmp = calc[start:end + 1]
        for i in range(len(tmp) - 1):
            del calc[start + 1]
        calc[start] = calculate(tmp)
    
    calculate(calc)

def findLastOccurence(someList, elem):
    return len(someList) - someList[-1::-1].index(elem) - 1

def findFirstOccurence(someList, elem):
    return someList.index(elem)

def calculate(calc):
    if('(' in calc and ')' in calc):
        calc.remove('(')
        calc.remove(')')

    operatorIndex1 = 0
    operatorIndex2 = 0

    if 'sqr' in calc and 'sqrt' in calc:
        while 'sqr' in calc and 'sqrt' in calc:
            operatorIndex1 = calc.index('sqr')
            operatorIndex2 = calc.index('sqrt')

            if operatorIndex1 < operatorIndex2:
                calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 -1]) * float(calc[operatorIndex1 -1]))
                del calc[operatorIndex1]
            elif operatorIndex2 < operatorIndex1:
                calc[operatorIndex2 - 1] = str(math.sqrt(float(calc[operatorIndex2 -1])))
                del calc[operatorIndex2]

    if 'sqr' in calc:
        while 'sqr' in calc:
            operatorIndex1 = calc.index('sqr')
            calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 -1]) * float(calc[operatorIndex1 -1]))
            del calc[operatorIndex1]
    if 'sqrt' in calc:
        while 'sqrt' in calc:
            operatorIndex2 = calc.index('sqrt')
            calc[operatorIndex2 - 1] = str(math.sqrt(float(calc[operatorIndex2 -1])))
            del calc[operatorIndex2]


    if '*' in calc and '/' in calc:
        while '*' in calc and '/' in calc:
            operatorIndex1 = calc.index('*')
            operatorIndex2 = calc.index('/')

            if operatorIndex1 < operatorIndex2:
                calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 - 1]) * float(calc[operatorIndex1 + 1]))
                del calc[operatorIndex1]
                del calc[operatorIndex1]
            elif operatorIndex2 < operatorIndex1:
                calc[operatorIndex2 - 1] = str(float(calc[operatorIndex2 - 1]) / float(calc[operatorIndex2 + 1]))
                del calc[operatorIndex2]
                del calc[operatorIndex2]

    if '*' in calc:
        while '*' in calc:
            operatorIndex1 = calc.index('*')
            calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 - 1]) * float(calc[operatorIndex1 + 1]))
            del calc[operatorIndex1]
            del calc[operatorIndex1]
    if '/' in calc:
        while '/' in calc:
            operatorIndex2 = calc.index('/')
            calc[operatorIndex2 - 1] = str(float(calc[operatorIndex2 - 1]) / float(calc[operatorIndex2 + 1]))
            del calc[operatorIndex2]
            del calc[operatorIndex2]

    if '+' in calc and '-' in calc:
        while '+' in calc and '-' in calc:
            operatorIndex1 = calc.index('+')
            operatorIndex2 = calc.index('-')

            if operatorIndex1 < operatorIndex2:
                calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 - 1]) + float(calc[operatorIndex1 + 1]))
                del calc[operatorIndex1]
                del calc[operatorIndex1]
            elif operatorIndex2 < operatorIndex1:
                calc[operatorIndex2 - 1] = str(float(calc[operatorIndex2 - 1]) - float(calc[operatorIndex2 + 1]))
                del calc[operatorIndex2]
                del calc[operatorIndex2]

    if '+' in calc:
        while '+' in calc:
            operatorIndex1 = calc.index('+')
            calc[operatorIndex1 - 1] = str(float(calc[operatorIndex1 - 1]) + float(calc[operatorIndex1 + 1]))
            del calc[operatorIndex1]
            del calc[operatorIndex1]
    if '-' in calc:
        while '-' in calc:
            operatorIndex2 = calc.index('-')
            calc[operatorIndex2 - 1] = str(float(calc[operatorIndex2 - 1]) - float(calc[operatorIndex2 + 1]))
            del calc[operatorIndex2]
            del calc[operatorIndex2]
    return str(calc[0])

operator = ""
calc = []
numUndos = 100
undo = []
line = ""

def button_click(number):
    global calc
    global undo
    global line
    
    if number.isdigit() or number == '.':
        line += str(number)
    else:
        if line != "":
            calc.append(line)
        calc.append(number)

        if len(undo) >= numUndos - 2:
            undo = undo[2:len(undo)]

        if line != "":
            undo.append(line)
        undo.append(number)
        line = ""
    
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + number)

def button_equal():
    global calc
    global undo
    global line
    current = entry.get()
    if line != "":
        calc.append(line)
    line = ""
    parse(calc)
    display.insert(tk.END, "\n" + current + " = " + calc[0])
    display.see("end")
    entry.delete(0, tk.END)
    entry.insert(0, calc[0])
    undo.append('=')
    undo.append(calc[0])
    
def button_undo():
    global undo
    global calc
   
    entry.delete(0, tk.END)

    if undo[len(undo) - 2] == '=':
        undo = undo[:len(undo) - 2]
    else:
        del undo[len(undo) - 1]

    if '=' in undo:
        startIndex = findLastOccurence(undo, '=') + 1
    else:
        startIndex = 0

    calc.clear()
    line = ""

    for index in range(startIndex, len(undo)):
        line += str(undo[index])
        calc.append(undo[index])

    entry.insert(0, line)

def button_add():
    global operator
    operator = '+'
    button_click(operator)
    
def button_mod():
    global operator
    operator = '%'
    button_click(operator)

def button_div():
    global operator
    operator = '/'
    button_click(operator)

def button_mult():
    global operator
    operator = '*'
    button_click(operator)

def button_min():
    global operator
    operator = '-'
    button_click(operator)

def button_sqr():
    global operator
    operator = 'sqr'
    button_click(operator)

def button_sqrt():
    global operator
    operator = 'sqrt'
    button_click(operator)

def button_clear():
    entry.delete(0, tk.END)
    calc.clear()

def keyPressed(event):
    button_click(event.char)

def returnPressed(event):
    button_equal()

#define windows
window = tk.Tk()
window.title("Simple Calculator")

display = tk.Text(master = window, height = 5, width = 35, borderwidth = 0)
display.grid(row = 0, column = 0, rowspan = 2, columnspan = 6, sticky = 'new')

entry = tk.Entry(master = window, width = 35, borderwidth = 0, font = ('Arial 20'))
entry.grid(row = 3, column = 0, columnspan = 6, sticky = 'new')
entry.grid_rowconfigure(1, weight = 1)
entry.grid_columnconfigure(0, weight = 1)

# Define buttons
btn_1 = tk.Button(master = window, text= "1", padx = 20, pady = 10, command = lambda: button_click('1'))
btn_2 = tk.Button(master = window, text= "2", padx = 20, pady = 10, command = lambda: button_click('2')) 
btn_3 = tk.Button(master = window, text= "3", padx = 20, pady = 10, command = lambda: button_click('3')) 
btn_4 = tk.Button(master = window, text= "4", padx = 20, pady = 10, command = lambda: button_click('4')) 
btn_5 = tk.Button(master = window, text= "5", padx = 20, pady = 10, command = lambda: button_click('5')) 
btn_6 = tk.Button(master = window, text= "6", padx = 20, pady = 10, command = lambda: button_click('6')) 
btn_7 = tk.Button(master = window, text= "7", padx = 20, pady = 10, command = lambda: button_click('7')) 
btn_8 = tk.Button(master = window, text= "8", padx = 20, pady = 10, command = lambda: button_click('8')) 
btn_9 = tk.Button(master = window, text= "9", padx = 20, pady = 10, command = lambda: button_click('9')) 
btn_0 = tk.Button(master = window, text= "0", padx = 20, pady = 10, command = lambda: button_click('0'))
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

# Detecting key presses
window.bind("<Key>", keyPressed)
window.bind('<Return>', returnPressed)
# main loop is applied at the end of the file
window.mainloop()