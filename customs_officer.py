import tkinter as tk
import os
from tkinter import messagebox

# create the main window
root = tk.Tk()
root.geometry('480x240')
root.title("Customs officer menu")
option_menu_frame = tk.Frame(root)
option_menu_frame.pack(padx=20, pady=20)

def enter_civil_id():
    root.withdraw()
    os.system("python3 enter_civil_id.py")

def see_report():
    root.withdraw()
    os.system("python3 report.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")

option_menu_label = tk.Label(option_menu_frame, text="Select an option:")
option_menu_label.pack(padx=5, pady=5)

existing_passenger_button = tk.Button(option_menu_frame, text="Enter Civil ID", command=enter_civil_id, bg='#023047',fg='white')
existing_passenger_button.pack(padx=5, pady=5)

new_passenger_button = tk.Button(option_menu_frame, text="See Report", command=see_report, bg='#023047',fg='white')
new_passenger_button.pack(padx=5, pady=5)


menubar = tk.Menu(root)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)

# run the main loop
root.mainloop()