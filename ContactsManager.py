print("\n" + "="*43)
print("         CONTACTS MANAGER")
print("="*43 + "\n")

import os

# Declarations
Table_prenom = [] 
Table_nom = [] 
Table_tele = []
Table_gmail = []
profil_num = -1
chois = 100

# Default output file path (current directory)
output_file_path = os.path.join(os.getcwd(), "contacts_output_file.txt")

# Functions
def PhonIcon():
    print("             //")
    print("            ///")

def menu_Bar():
    print("__________________________________CONTACT LIST___________________________________")
    print("|     LAST NAME     |     FIRST NAME    |   PHONE   |         EMAIL ADDRESS       |")

def pasTrouver_Bar():
    print("|                                                                                 |")
    print("|                           !! No contact found !!                                |")

def finaly_Bar():
    print("|_________________________________________________________________________________|")

def sauvegard_contacts():
    global output_file_path
    with open(output_file_path, "w") as fichier:
        fichier.write("____________________________________CONTACTS_____________________________________\n")
        for i in range(profil_num + 1):
            fichier.write(f"| {Table_nom[i]:<17}| {Table_prenom[i]:<17}| {Table_tele[i]:<11}| {Table_gmail[i]:<29}|")
        fichier.write("|_________________________________________________________________________________|")

def changer_chemin_fichier():
    global output_file_path
    while True:
        print("Current path:", output_file_path)
        print("(1) Enter a new path")
        print("(0) Back to main menu")
        choix = input("Select an option: ")
        if choix == '0':
            break
        elif choix == '1':
            nouveau_chemin = input("Enter the new path for saving the contacts file (with .txt):\n").strip()
            if not nouveau_chemin.endswith(".txt"):
                print("Error: The file must end with .txt")
            else:
                try:
                    with open(nouveau_chemin, "a"): pass
                    output_file_path = nouveau_chemin
                    print("Output file path successfully updated to:", output_file_path)
                    break
                except Exception as e:
                    print("Error: Unable to use the given path.\n", e)
        else:
            print("Invalid option. Please choose 0 or 1.")

# Main Program Loop
while chois != 'x':
    print("________MAIN MENU________")
    print("(1) Add a contact")
    print("(2) Display all contacts")
    print("(3) Search for a contact")
    print("(4) Manage a contact")
    print("(5) About this program")
    print("(6) Edit database output file")
    print("(x) Exit the program")
    chois = input("Select an option: ")

    match chois:
        case '1':
            profil_num += 1
            print("________ADD CONTACT________")
            prenom = input("First name: ")
            nom = input("Last name (IN UPPERCASE): ").upper()
            tele = input("Phone number: ")
            while len(tele) != 10:
                print("Phone number must contain exactly 10 digits!")
                tele = input("Phone number: ")
            Email = input("Enter your email: ")
            while not (Email.endswith("@gmail.com") or Email.endswith("@e-mail.com") or Email.endswith("@outlook.fr")):
                print("Invalid email address!")
                print("Email must end with '@gmail.com', '@e-mail.com', or '@outlook.fr'")
                Email = input("Enter your email: ")
            Table_prenom.insert(profil_num, prenom)
            Table_nom.insert(profil_num, nom)
            Table_tele.insert(profil_num, tele)
            Table_gmail.insert(profil_num, Email)
            print(f"{nom} {prenom} has been successfully added to your contacts.")

        case '2':
            if profil_num > -1:
                menu_Bar()
                for i in range(profil_num + 1):
                    print(f"| {Table_nom[i]:<17}| {Table_prenom[i]:<17}| {Table_tele[i]:<11}| {Table_gmail[i]:<29}|")
                finaly_Bar()
            else:
                menu_Bar()
                pasTrouver_Bar()
                finaly_Bar()

        case '3':
            print("________SEARCH CONTACTS________")
            while True:
                print("(1) Search by last name")
                print("(2) Search by first name")
                print("(3) Search by phone number")
                print("(0) Back to main menu")
                type_cherche = input("Select a search method: ")
                if type_cherche == '0':
                    break
                estTrouve = False
                menu_Bar()
                if type_cherche == '1':
                    fond_nom = input("Enter the last name (IN UPPERCASE): ").upper()
                    for i in range(profil_num + 1):
                        if fond_nom == Table_nom[i]:
                            print(f"| {Table_nom[i]:<17}| {Table_prenom[i]:<17}| {Table_tele[i]:<11}| {Table_gmail[i]:<29}|")
                            estTrouve = True
                elif type_cherche == '2':
                    fond_prenom = input("Enter the first name: ")
                    for i in range(profil_num + 1):
                        if fond_prenom == Table_prenom[i]:
                            print(f"| {Table_nom[i]:<17}| {Table_prenom[i]:<17}| {Table_tele[i]:<11}| {Table_gmail[i]:<29}|")
                            estTrouve = True
                elif type_cherche == '3':
                    fond_tele = input("Enter the phone number: ")
                    for i in range(profil_num + 1):
                        if fond_tele == Table_tele[i]:
                            print(f"| {Table_nom[i]:<17}| {Table_prenom[i]:<17}| {Table_tele[i]:<11}| {Table_gmail[i]:<29}|")
                            estTrouve = True
                if not estTrouve:
                    pasTrouver_Bar()
                finaly_Bar()

        case '4':
            print("Manage contact feature is under development.")

        case '5':
            print("This program helps manage your contacts with the following features:")
            print("1) Add a new contact")
            print("2) View all contacts")
            print("3) Search for specific contacts")
            print("4) Manage or edit existing contacts")
            print("5) Change the file path where contacts are saved")
            print("6) Exit the program")
            note = input("\nHow would you rate this program (1-10)?\n")
            print("Thank you for your feedback!")

        case '6':
            changer_chemin_fichier()

    print("\n")
    sauvegard_contacts()
