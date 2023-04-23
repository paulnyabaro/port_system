import tkinter as tk

app = tk.Tk()

app.geometry('720x480')
app.title('Port System Login')


def login_user():
    print('The username entered is ' + str(username_var) + 'and the password is ' + str(password_var))
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