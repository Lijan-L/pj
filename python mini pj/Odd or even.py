import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        num = int(fname.get())  # Get the number entered in the Entry widget and convert to integer
        if num % 2 == 0:
            messagebox.showinfo("Result", f"The number {num} is even")
        else:
            messagebox.showinfo("Result", f"The number {num} is odd")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

calc = tk.Tk()
calc.title("Odd or even")
calc.geometry("300x150")

nl = tk.Label(calc, text="Enter a number:")
nl.pack()

fname = tk.Entry(calc)
fname.pack()

button = tk.Button(calc, text="Check", command=check_number)
button.pack()

calc.mainloop()