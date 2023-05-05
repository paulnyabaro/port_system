# port_system
## Introduction
The Port System is a project built in Python using the Tkinter library for graphical user interface (GUI) development. The system has been designed to facilitate the management of passengers entering and leaving a port, with two types of users: immigration officers and custom officers. The system utilizes two text files: login.txt and passenger.txt. The login.txt file contains users' credentials, including their username, password, and role. The passenger.txt file stores passenger data in a dictionary format. Each passenger's unique Civil Id serves as the key, and the remaining fields include name, date of birth, gender, custom fine, and status.

The project begins with a login screen where users enter their credentials. Once authenticated, the user is directed to their respective dashboard, where they can access the various features of the system.

##Immigration Officer Dashboard
The immigration officer is presented with a menu containing four options: existing passenger, new passenger, search passenger, and logout. Choosing the existing passenger option takes the officer to a screen where they can enter the Civil Id of the passenger they are looking for. If the passenger is found in the system, the officer can view all the passenger's details. They are also presented with a menu to update the passenger's status to one of four options: Arrival Rejected, Arrival Approved, Departure Rejected, and Departure Approved. 

If the immigration officer selects the new passenger option, they are directed to a screen where they can enter the new passenger's details, excluding the custom fine and status fields, which are set to blank. The system then stores the passenger's data in the passenger.txt file. Choosing the search passenger option provides the same functionality as the existing passenger option, but without the status update feature. The logout option takes the user back to the login screen.

##Custom Officer Dashboard
The custom officer dashboard provides three menu options: enter Civil Id, see report, and logout. Selecting the enter Civil Id option takes the officer to a screen like the existing passenger option for immigration officers, but with three options: allow through green channel, passenger self-declared items, and inspect item. Choosing the allow through green channel or passenger self-declared items options sets the custom fine field to zero, while selecting the inspect item option allows the officer to enter a custom fine amount that is saved to the file.
Choosing the see report option takes the custom officer to a page where they can view the total number of passengers fined, the average fine per passenger, and the number of passengers with fines over 6000. The logout option takes the user back to the login screen.

##Conclusion
The Port System project provides an efficient and user-friendly solution for managing passengers entering and leaving a port. The system has been designed with two types of users in mind: immigration officers and custom officers. Each user has a unique dashboard, providing them with the necessary functionality to carry out their duties effectively. The project utilizes two text files to store user credentials and passenger data, respectively, providing a reliable and scalable solution for port management. Overall, the Port System project provides an excellent example of how Python and Tkinter can be used to create robust and efficient software solutions.