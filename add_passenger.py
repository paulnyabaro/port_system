import tkinter as tk

def add_passenger():
    civil_id = entry_civil_id.get()
    name = entry_name.get()
    dob = entry_dob.get()
    gender = entry_gender.get()
    customs_fine = entry_customs_fine.get()
    status = entry_status.get()
    
    # Open file in append mode
    with open('passenger.txt', 'a') as f:
        # Write new record as a string to the end of the file
        f.write(f"{civil_id},{name},{dob},{gender},{customs_fine},{status}\n")
        
    # Clear the entry fields
    entry_civil_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_customs_fine.delete(0, tk.END)
    entry_status.delete(0, tk.END)

# Create tkinter window and widgets
root = tk.Tk()
root.title("Add passenger")

label_civil_id = tk.Label(root, text="Civil ID:")
entry_civil_id = tk.Entry(root)

label_name = tk.Label(root, text="Name:")
entry_name = tk.Entry(root)

label_dob = tk.Label(root, text="Date of Birth:")
entry_dob = tk.Entry(root)

label_gender = tk.Label(root, text="Gender:")
entry_gender = tk.Entry(root)

label_customs_fine = tk.Label(root, text="Customs Fine:")
entry_customs_fine = tk.Entry(root)

label_status = tk.Label(root, text="Status:")
entry_status = tk.Entry(root)

button_add = tk.Button(root, text="Add Passenger", command=add_passenger)

# Display widgets using grid layout
label_civil_id.grid(row=0, column=0)
entry_civil_id.grid(row=0, column=1)

label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)

label_dob.grid(row=2, column=0)
entry_dob.grid(row=2, column=1)

label_gender.grid(row=3, column=0)
entry_gender.grid(row=3, column=1)

label_customs_fine.grid(row=4, column=0)
entry_customs_fine.grid(row=4, column=1)

label_status.grid(row=5, column=0)
entry_status.grid(row=5, column=1)

button_add.grid(row=6, column=1)

root.mainloop()
