import tkinter as tk
from tkinter import messagebox

def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Macronomicon")

# Set window size (width x height)
root.geometry('400x200')

# Creating a label widget
my_label = tk.Label(root, text="Welcome to Macronomicon!")
my_label.pack()

# Creating a close button
close_button = tk.Button(root, text="Close", command=on_close)
close_button.pack()

# Run the application
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
