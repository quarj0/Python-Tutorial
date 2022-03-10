from time import *
from tkinter import *

# Importing modules

root = Tk()

root.title('Clock')


def timer():  # Defining our time
    string = strftime('%H:%M:%S %a')
    label.config(text=string)
    label.after(1000, timer)


# Labeling and packing

label = Label(root, font=('ds-digital', 80), background='black', foreground='cyan')
label.pack(anchor='center')
timer()

mainloop()
