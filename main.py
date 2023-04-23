import tkinter as tk

app = tk.Tk()

app.geometry('720x360')
app.title('Port System Login')

username_label = tk.Label(app, text='Username', font=('Arial', 14))
username_label.pack(padx=10, pady=10)

username_field = tk.Entry(app)
username_field.pack(padx=20, pady=10)

password_label = tk.Label(app, text='Password', font=('Arial', 14))
password_label.pack(padx=10, pady=10)

password_field = tk.Entry(app)
password_field.pack(padx=20, pady=10)

username_label = tk.Button(app, text='Login', font=('Arial', 14))
username_label.pack(padx=20, pady=10)

menuframe = tk.Frame(app)
menuframe.columnconfigure(0, weight=1)
menuframe.columnconfigure(1, weight=1)
menuframe.columnconfigure(2, weight=1)

menuitem1 = tk.Button(menuframe, text='Existing passenger', font=('Arial', 14))
menuitem1.grid(row=0, column=0, sticky=tk.W+tk.E)

menuitem2 = tk.Button(menuframe, text='New passenger', font=('Arial', 14))
menuitem2.grid(row=0, column=1, sticky=tk.W+tk.E)

menuitem3 = tk.Button(menuframe, text='Search Passenger', font=('Arial', 14))
menuitem3.grid(row=0, column=2, sticky=tk.W+tk.E)

menuitem4 = tk.Button(menuframe, text='Logout', font=('Arial', 14))
menuitem4.grid(row=0, column=3, sticky=tk.W+tk.E)

menuframe.pack(fill='x')

def login_user():
    with open("login.txt", 'r') as file:
        next(file)
        
        # iterate over the lines in the file
        for line in file:
            # remove any leading or trailing whitespace and split the line into fields
            fields = line.strip().split(',')
            
            # extract the fields and assign them to variables
            username = fields[0]
            password = fields[1]
            id = int(fields[2])
            role = fields[3]
            
            # do something with the data, e.g. print it
            print(f"Username: {username}, Password: {password}, ID: {id}, Role: {role}")




# Run app
app.mainloop()