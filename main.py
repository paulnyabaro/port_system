import tkinter as tk
import customtkinter

def login_user():
    pass

# System settings
customtkinter.set_appearance_mode("System") # Setting the dark or light mode from the system
customtkinter.set_default_color_theme("blue")


# Our app frame
app = customtkinter.CTk() # Initializing the app
app.geometry("720x480") # Setting the app size
app.title("Port System")


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Username")
title.pack(padx=10, pady=10) # Padding for x and y
 

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()


# Download button
download = customtkinter.CTkButton(app, text="Login", command=login_user) # Run function
download.pack(padx=10, pady=10) # .pack is used to make elements show up on the screen

# Run app
app.mainloop()