import tkinter as tk
from tkinter import messagebox
import os

# create a tkinter window
root = tk.Tk()
root.title("Passenger Information")

set_st = tk.StringVar()
set_st.set('')


# read the data from passenger.txt file
with open("passenger.txt", "r") as f:
    data = f.readlines()

# create a dictionary to store the data
passengers = {}
for line in data:
    line = line.strip().split(",")
    key = line[0]
    value = line[1:]
    passengers[key] = value

# create a function to display the passenger information
def display_info():
    # get the civil id entered by the user
    civil_id = entry.get()

    # check if the civil id exists in the passenger dictionary
    if civil_id in passengers:
        # get the passenger information
        info = passengers[civil_id]
        name = info[0]
        dob = info[1]
        gender = info[2]
        customs_fine = info[3]
        status = info[4]

        # display the passenger information on the screen
        name_label.config(text="Name: " + name)
        dob_label.config(text="Date of Birth: " + dob)
        gender_label.config(text="Gender: " + gender)
        customs_fine_label.config(text="Customs Fine: " + customs_fine)
        status_label.config(text="Status: " + status)

        def set_status(status):
            print('Status set to')

        set_status_frame = tk.LabelFrame(root, text='Set status', padx=20, pady=20)
        set_status_frame.grid(row=10, column=0, padx=20, pady=10)

        arrival_approved_r_button = tk.Radiobutton(set_status_frame, text="Arrival Approved", variable=set_st, value='Arrival Approved')
        arrival_approved_r_button.grid(row=8, column=0)

        arrival_rejected_r_button = tk.Radiobutton(set_status_frame, text="Arrival Rejected", variable=set_st, value='Arrival Rejected')
        arrival_rejected_r_button.grid(row=9, column=0)

        departure_approved_r_button = tk.Radiobutton(set_status_frame, text="Departure Approved", variable=set_st, value='Departure Approved')
        departure_approved_r_button.grid(row=10, column=0)


        departure_rejected_r_button = tk.Radiobutton(set_status_frame, text="Departure Rejected", variable=set_st, value='Departure Rejected')
        departure_rejected_r_button.grid(row=11, column=0)

        # back_button = tk.Button(set_status_frame, text="Go Back to previous menu")
        # back_button.grid(row=8, column=4)

        back_button = tk.Button(set_status_frame, text="Update Status", command=lambda:set_status('Arrival Approved'))
        back_button.grid(row=12, column=0, pady=10)

    else:
        # if the civil id does not exist in the passenger dictionary, display an error message
        # error_label.message(text="Passenger not found")
        tk.messagebox.showerror("Error", "Passenger not found")

def back_to_previous_menu():
    root.withdraw()
    os.system("python3 immigration_officer.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")

# create a label and entry widget for civil id

existing_customer_search_frame = tk.LabelFrame(root, text='Exiting passenger', padx=10, pady=10)
existing_customer_search_frame.grid(row=0, column=0, padx=10, pady=10)

id_label = tk.Label(existing_customer_search_frame, text="Enter Civil ID:")
id_label.grid(row=0, column=0)

entry = tk.Entry(existing_customer_search_frame)
entry.grid(row=0, column=1)
# entry.insert(0, 'Civil ID')

# create a button to display passenger information
button = tk.Button(existing_customer_search_frame, text="Search", command=display_info)
button.grid(row=0, column=2)


# create labels to display passenger information
name_label = tk.Label(root)
name_label.grid(row=2, column=0)

dob_label = tk.Label(root)
dob_label.grid(row=3, column=0)

gender_label = tk.Label(root)
gender_label.grid(row=4, column=0)

customs_fine_label = tk.Label(root)
customs_fine_label.grid(row=5, column=0)

status_label = tk.Label(root)
status_label.grid(row=6, column=0)


menubar = tk.Menu(root)
menubar.add_command(label='Go Back', command=back_to_previous_menu)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)



# start the tkinter main loop
root.mainloop()
