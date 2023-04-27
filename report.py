import tkinter as tk
import json
import os

# create a tkinter window
root = tk.Tk()
root.title("Report")


report_frame = tk.LabelFrame(root, text='Passenger custom fine report', padx=10, pady=10)
report_frame.grid(row=0, column=0, padx=10, pady=10)

# create labels to display passenger information
total_passengers_fined_label = tk.Label(report_frame)
total_passengers_fined_label.grid(row=1, column=0)

average_fine_per_passenger_label = tk.Label(report_frame)
average_fine_per_passenger_label.grid(row=2, column=0)

passengers_with_fine_over_label = tk.Label(report_frame)
passengers_with_fine_over_label.grid(row=3, column=0)

# read the data from passenger.txt file
with open("passenger.txt", "r") as f:
    passengers = json.load(f)

# create a function to display the passenger information
# def display_info():
    # get the civil id entered by the user
    # civil_id = entry.get()

    # info = passengers[civil_id]
total_passengers_fined = 10
average_fine_per_passenger = 1500
passengers_with_fine_over = 5
# customs_fine = info[3]

# display the passenger information on the screen
total_passengers_fined_label.config(text="Total passengers fined: " + str(total_passengers_fined))
average_fine_per_passenger_label.config(text="Average fine per passenger: " + str(average_fine_per_passenger) + " KD")
passengers_with_fine_over_label.config(text="Passengers with fine more than 6000 KD: " + str(passengers_with_fine_over))

def set_status(status):
    print('Status set to')




def back_to_previous_menu():
    root.withdraw()
    os.system("python3 customs_officer.py")

def logout_user():
    root.withdraw()
    os.system("python3 main.py")






menubar = tk.Menu(root)
menubar.add_command(label='Go Back', command=back_to_previous_menu)
menubar.add_command(label='Logout', command=logout_user)
root.config(menu=menubar)


# start the tkinter main loop
root.mainloop()
