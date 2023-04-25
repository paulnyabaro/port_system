import tkinter as tk

# create a tkinter window
root = tk.Tk()
root.title("Inspect Item")

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


    else:
        # if the civil id does not exist in the passenger dictionary, display an error message
        error_label.config(text="Passenger not found")

# create a label and entry widget for civil id
id_label = tk.Label(root, text="Set custom fine:")
id_label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)
# entry.insert(0, 'Civil ID')

# create a button to display passenger information
button = tk.Button(root, text="Display Information", command=display_info)
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


# create an error label
error_label = tk.Label(root, fg="red")
error_label.grid(row=6, column=0)


# start the tkinter main loop
root.mainloop()
