import tkinter as tk
from tkinter import messagebox
import os

# create the main window
root = tk.Tk()
root.geometry('480x240')
root.title("Port System Login")

# create the login frame
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

# create the login labels and entries
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)


# create the login button function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # check the login credentials
    with open("login.txt", "r") as f:
        for line in f:
            line = line.strip().split(",")
            if username == line[0] and password == line[1]:
                role = line[3]
                break
        else:
            tk.messagebox.showerror("Error", "Invalid username or password")
            return
    
    # destroy the login frame and create the option menu frame
    login_frame.destroy()
    option_menu_frame = tk.Frame(root)
    option_menu_frame.pack(padx=20, pady=20)
    
    # create the option menu for the Immigration officer
    if role == "Customs officer":
        root.destroy()
        os.system("python3 customs_officer.py")

    elif role == "Immigration officer":
        root.destroy()
        os.system("python3 immigration_officer.py")


def existing_passenger():
    print('Existing customer')

def logout():
    login_frame.pack()

# create the login button
login_button = tk.Button(login_frame, text="Login", command=login, bg='blue', padx=50, pady=10)
login_button.grid(row=2, column=1)

# run the main loop
root.mainloop()