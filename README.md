# Generation of Calibration File 

[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)

The objective of this project is to create an address book using Python and a database
database to store contact information. 

## Utilization

### - Main Loop

The main loop presents a menu to the user with options to add, display, delete, modify, or search for contacts. It repeatedly prompts the user for input and performs the corresponding action based on the selected option. The loop continues until the user chooses to exit by entering '0'. Each option invokes methods from the mon_action object, which represents actions on contacts in a database. The actions include adding, displaying, deleting, and modifying contact information.

### 1- Add a contact

The code defines a method ajouter_contacte to add a new contact to a database. It prompts the user to input details such as name, gender, email, phone number, address, and country. The information is then inserted into a database table named "contacte," including a default value for the "imageID" column.

### 2- Display contact list

The code defines a method afficher_les_contactes to retrieve and display all contacts from a database table named "contacte." It fetches all rows from the table and prints the results. The method then commits the changes to the database.

### 3- Delete a contact

The code defines a method supprimer_contacte to delete a contact from a database table named "contacte." It prompts the user for the name of the contact to be deleted, performs the deletion using a SQL DELETE statement with a parameterized query, and then prints a confirmation message. Finally, the method commits the changes to the database.

### 4- Edit contacts

The code defines a method modifier_contacte to interactively modify specific elements of a contact in a database table named "contacte." It prompts the user to select an element (e.g., name, email, etc.) and enter a new value. The method then constructs and executes an SQL UPDATE statement to modify the corresponding column for the found contact. The process continues until the user chooses to exit. If no contact is found, it prints a message indicating that no contact was found.

### 5- Find a contact

The code defines a method recherche_contacte to search for a contact in a database table named "contacte" based on the provided name. It executes an SQL SELECT statement and prints the contact details if found. The method returns the value of the second column (index 1) of the found row or None if no contact is found. If an exception occurs during execution, it prints an error message.

## Start

### 1- Testing execution with .exe

This program containe a executable file of the name "createHexFile.exe". 
It has the following path : 
```shell
C:\Users\alexandre.puiseux> C:\...\GenerateCalibration2\build\exe.win-amd64-3.7\createHexFile.exe
```
It will execute the program with one argument, exactly like the part 1 of Utilisation.

### 2- Use execution with .exe

```shell
C:\Users\alexandre.puiseux> C:\...\GenerateCalibration2\build\exe.win-amd64-3.7\createHexFile.exe C:/link/of/the/excel/file.xlsm fistAddress sizeOfData defaultValues excelSheet
```
The code will this time created a new Calibration File of the excel file you wich, next to it. This way, the code can also be use in the cmd, or it can be call and use in any other code (Php, JavaScript, ect...). 

### 3- Help
```shell
C:\Users\alexandre.puiseux> C:\...\GenerateCalibration2\build\exe.win-amd64-3.7\createHexFile.exe -h
```
In last, you can also see the command and more information on how to use this code by use the argument -h or --help.

## Build with

* [Pyhton.py](https://www.python.org/) - Python (back-end)
* [SQlite](https://www.sqlite.org/docs.html) - SQlite (BDD)
* [Visual Studio Code](https://code.visualstudio.com/) - IDE

## Contributing

* **Joan-Baptiste FERRANDO** (https://www.linkedin.com/in/joan-baptiste-ferrando-980b23290/)

## Versions

**Last version :** 1.0

## Author

* **Alexandre Puiseux** _alias_[@AlexandrePuiseux65](https://github.com/AlexandrePuiseux65)
* **Joan-Baptiste FERRANDO** _alias_[@joan-b-f](https://github.com/joan-b-f)

## License

Within the scope of the second-year bachelor's project, this tool was crafted to address the requirements of December's Hackathon. Further details can be found in the accompanying license documentation.

[LICENSE](LICENSE)

![Alt Text](https://media.giphy.com/media/3orif4LwcbQhWZVsze/giphy.gif)
