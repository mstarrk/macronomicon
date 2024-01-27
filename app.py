import tkinter
import customtkinter

# sys settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

# frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Macronomicon")

# ui elements
title = customtkinter.CTkLabel(app, text="Hello world", font=("Arial", 32))
text = customtkinter.CTkEntry(app, width=350, height=40)

title.pack()
text.pack()

# run app
app.mainloop()
