import tkinter as tk
from tkinter import messagebox
import json
import os

# create a tkinter window
root = tk.Tk()
root.title("Civil ID")

set_st = tk.StringVar()
set_st.set('')


# read the data from passenger.txt file
with open("passenger.txt", "r") as f:
    passengers = json.load(f)

# # create a dictionary to store the data
# passengers = {}
# for line in data:
#     line = line.strip().split(",")
#     key = line[0]
#     value = line[1:]
#     passengers[key] = value

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

        def set_custom_fine_zero(custom_fine_amount):
            with open('passenger.txt', 'r') as f:
                passengers = json.load(f)
                del passengers[f"{civil_id}"]
                customs_fine = custom_fine_amount
                # Write new record as a string to the end of the file
                new_passenger_data = f"\"{civil_id}\": [\"{name}\", \"{dob}\", \"{gender}\", \"{customs_fine}\", \"{status}\"\n]"
                json_string_data = "{" + new_passenger_data + "}"
                new_passenger_data_json = json.loads(json_string_data)
                passengers.update(new_passenger_data_json)

            with open('passenger.txt', 'w') as f:
                # f.write(json.dumps(passengers, indent=None))
                # f.write('\n')
                f.write("{\n")
                for i, (key, value) in enumerate(passengers.items()):
                    json_string = json.dumps({key: value})
                    if i == len(passengers) - 1:
                        f.write(f"    {json_string[1:-1]}\n")
                    else:
                        f.write(f"    {json_string[1:-1]},\n")
                f.write("}\n")
            
            tk.messagebox.showinfo("Success", "Custom fine updated to 0")
        

        def set_custom_fine_amount():
            with open('passenger.txt', 'r') as f:
                passengers = json.load(f)
                del passengers[f"{civil_id}"]
                customs_fine = inspect_custom_fine_entry.get()
                # Write new record as a string to the end of the file
                new_passenger_data = f"\"{civil_id}\": [\"{name}\", \"{dob}\", \"{gender}\", \"{customs_fine}\", \"{status}\"\n]"
                json_string_data = "{" + new_passenger_data + "}"
                new_passenger_data_json = json.loads(json_string_data)
                passengers.update(new_passenger_data_json)

            with open('passenger.txt', 'w') as f:
                # f.write(json.dumps(passengers, indent=None))
                # f.write('\n')
                f.write("{\n")
                for i, (key, value) in enumerate(passengers.items()):
                    json_string = json.dumps({key: value})
                    if i == len(passengers) - 1:
                        f.write(f"    {json_string[1:-1]}\n")
                    else:
                        f.write(f"    {json_string[1:-1]},\n")
                f.write("}\n")
            
            tk.messagebox.showinfo("Success", f"Custom fine updated to {customs_fine}")
        

        set_status_frame = tk.LabelFrame(root, text='Custom fine field', padx=20, pady=20)
        set_status_frame.grid(row=10, column=0, padx=20, pady=10)

        allow_through_green_channel = tk.Button(set_status_frame, text="Allow through green channel", command=lambda:set_custom_fine_zero(0))
        allow_through_green_channel.grid(row=1, column=0)

        allow_through_green_channel = tk.Button(set_status_frame, text="Passenger self declared items", command=lambda:set_custom_fine_zero(0))
        allow_through_green_channel.grid(row=2, column=0)


        inspect_item_frame = tk.LabelFrame(root, text='Inspect Item', padx=20, pady=20)
        inspect_item_frame.grid(row=12, column=0, padx=20, pady=10)

        inspect_custom_fine_entry = tk.Entry(inspect_item_frame)
        inspect_custom_fine_entry.grid(row=1, column=0)

        allow_through_green_channel = tk.Button(inspect_item_frame, text="Set Fine", command=lambda:set_custom_fine_amount())
        allow_through_green_channel.grid(row=1, column=1)

    else:
        # if the civil id does not exist in the passenger dictionary, display an error message
        # error_label.message(text="Passenger not found")
        tk.messagebox.showerror("Error", "Passenger not found")



def back_to_previous_menu():
    root.withdraw()
    os.system("python3 customs_officer.py")

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
