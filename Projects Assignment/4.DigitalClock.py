# Digital Clock
# Create a digital clock GUI application with Python.

from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("400x400")
root.resizable(0, 0)

# Set a background color or image
root.configure(bg='yellow')

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

# Create a label for the clock with enhanced styling
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan", bd=10, relief=SUNKEN)
label.pack(anchor='center', pady=20)

# Add a title label
title_label = Label(root, text="Current Time", font=("Arial", 24), background='yellow', foreground='black')
title_label.pack(anchor='center')

time()

root.mainloop()
