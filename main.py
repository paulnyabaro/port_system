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
app.title("Port System Login")


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Username")
title.pack(padx=10, pady=10) # Padding for x and y

# Link input
username_var = tk.StringVar() # Getting the value of the link input
username = customtkinter.CTkEntry(app, width=350, height=40, textvariable=username_var) # app is where to place it -> inside the app
username.pack()

# Adding UI elements
title = customtkinter.CTkLabel(app, text="Password")
title.pack(padx=10, pady=10) # Padding for x and y

# Link input
password_var = tk.StringVar() # Getting the value of the link input
password = customtkinter.CTkEntry(app, width=350, height=40, textvariable=password_var) # app is where to place it -> inside the app
password.pack()

# Download button
download = customtkinter.CTkButton(app, text="Login", command=login_user) # Run function
download.pack(padx=20, pady=20) # .pack is used to make elements show up on the screen

# Run app
app.mainloop()