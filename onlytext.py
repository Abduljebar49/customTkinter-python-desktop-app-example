import tkinter as tk
from tkinter import messagebox

def validate_entry(text):
    if text.isdigit() and 0 <= int(text) <= 100:
        return True
    else:
        messagebox.showerror("Invalid Input", "Please enter a number between 0 and 100.")
        return False

def handle_entry(event):
    if not validate_entry(entry.get()):
        entry.delete(0, tk.END)

root = tk.Tk()

validation = root.register(validate_entry)

entry = tk.Entry(root, validate="focusout", validatecommand=(validation, '%P'))
entry.pack()

entry.bind('<FocusOut>', handle_entry)

root.mainloop()