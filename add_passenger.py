import tkinter as tk
import json
import os
from tkinter import messagebox


def add_passenger():
    civil_id = entry_civil_id.get()
    name = entry_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    customs_fine = ''
    status = ''
    
    # Open file in append mode
    with open('passenger.txt', 'r') as f:
        passengers = json.load(f)
        # Write new record as a string to the end of the file
        new_passenger_data = f"\"{civil_id}\": [\"{name}\", \"{dob}\", \"{gender}\", \"{customs_fine}\", \"{status}\"\n]"
        json_string_data = "{" + new_passenger_data + "}"
        new_passenger_data_json = json.loads(json_string_data)
        passengers.update(new_passenger_data_json)

    with open('passenger.txt', 'w') as f:
        f.write("{\n")
        for i, (key, value) in enumerate(passengers.items()):
            json_string = json.dumps({key: value})
            if i == len(passengers) - 1:
                f.write(f"    {json_string[1:-1]}\n")
            else:
                f.write(f"    {json_string[1:-1]},\n")
        f.write("}\n")

    tk.messagebox.showinfo("Success", f"Passenger {name} added successfully!")

    # Clear the entry fields
    entry_civil_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    # entry_customs_fine.delete(0, tk.END)
    # entry_status.delete(0, tk.END)

def back_to_previous_menu():
    root.withdraw()
    os.system("python3 immigration_officer.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")

# Create tkinter window and widgets
root = tk.Tk()
root.title("Add passenger")
root.geometry('480x240')

label_civil_id = tk.Label(root, text="Civil ID:")
entry_civil_id = tk.Entry(root)

label_name = tk.Label(root, text="Name:")
entry_name = tk.Entry(root)

label_dob = tk.Label(root, text="Date of Birth:")
entry_dob = tk.Entry(root)

label_gender = tk.Label(root, text="Gender:")
entry_gender = tk.Entry(root)

# label_customs_fine = tk.Label(root, text="Customs Fine:")
# entry_customs_fine = tk.Entry(root)

# label_status = tk.Label(root, text="Status:")
# entry_status = tk.Entry(root)

button_add = tk.Button(root, text="Add Passenger", command=add_passenger, bg='#023047',fg='white')

# Display widgets using grid layout
label_civil_id.grid(row=0, column=0)
entry_civil_id.grid(row=0, column=1)

label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)

label_dob.grid(row=2, column=0)
entry_dob.grid(row=2, column=1)

label_gender.grid(row=3, column=0)
entry_gender.grid(row=3, column=1)

# label_customs_fine.grid(row=4, column=0)
# entry_customs_fine.grid(row=4, column=1)

# label_status.grid(row=5, column=0)
# entry_status.grid(row=5, column=1)

menubar = tk.Menu(root)
menubar.add_command(label='Go Back', command=back_to_previous_menu)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)

button_add.grid(row=6, column=1)

root.mainloop()
