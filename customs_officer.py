import tkinter as tk
import os
from tkinter import messagebox

# create the main window
root = tk.Tk()
root.geometry('480x240')
root.title("Customs officer menu")
option_menu_frame = tk.Frame(root)
option_menu_frame.pack(padx=20, pady=20)

def search_passenger():
    root.withdraw()
    os.system("python3 search_passenger.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")

option_menu_label = tk.Label(option_menu_frame, text="Select an option:")
option_menu_label.pack(padx=5, pady=5)

existing_passenger_button = tk.Button(option_menu_frame, text="Enter Civil ID")
existing_passenger_button.pack(padx=5, pady=5)

new_passenger_button = tk.Button(option_menu_frame, text="See Report")
new_passenger_button.pack(padx=5, pady=5)

logout_button = tk.Button(option_menu_frame, text="Logout", command=logout_user)
logout_button.pack(padx=5, pady=5)

menubar = tk.Menu(root)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)

# run the main loop
root.mainloop()