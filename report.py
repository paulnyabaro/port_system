import tkinter as tk
import os

# create a tkinter window
root = tk.Tk()
root.title("Report")

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
        customs_fine = info[3]

        # display the passenger information on the screen
        name_label.config(text="Total customers fined: " + name)
        dob_label.config(text="Average fine per passenger: " + dob)
        customs_fine_label.config(text="Passengers with fine more than 6000 KD: " + customs_fine)

        def set_status(status):
            print('Status set to')




def back_to_previous_menu():
    root.withdraw()
    os.system("python3 customs_officer.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")

# create a label and entry widget for civil id
id_label = tk.Label(root, text="Set custom fine:")
id_label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)
# entry.insert(0, 'Civil ID')

# create a button to display passenger information
button = tk.Button(root, text="Set", command=display_info)
button.grid(row=0, column=2)

# create labels to display passenger information
name_label = tk.Label(root)
name_label.grid(row=1, column=0)

dob_label = tk.Label(root)
dob_label.grid(row=2, column=0)

gender_label = tk.Label(root)
gender_label.grid(row=3, column=0)

customs_fine_label = tk.Label(root)
customs_fine_label.grid(row=4, column=0)

status_label = tk.Label(root)
status_label.grid(row=5, column=0)

menubar = tk.Menu(root)
menubar.add_command(label='Go Back', command=back_to_previous_menu)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)


# start the tkinter main loop
root.mainloop()
