# Simple Interest Calculator
# Create Simple Interest Calculator GUI application with Python.

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("400x400")
root.resizable(0,0)

def calculate_si():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    si = (principal * rate * time) / 100
    messagebox.showinfo("Simple Interest", f"Simple Interest: {si}")

principal_label = Label(root, text="Principal Amount:")
principal_label.pack()

principal_entry = Entry(root)
principal_entry.pack()

rate_label = Label(root, text="Rate of Interest:")
rate_label.pack()

rate_entry = Entry(root)
rate_entry.pack()

time_label = Label(root, text="Time (in years):")
time_label.pack()

time_entry = Entry(root)
time_entry.pack()

calculate_button = Button(root, text="Calculate", command=calculate_si)
calculate_button.pack()

root.mainloop()