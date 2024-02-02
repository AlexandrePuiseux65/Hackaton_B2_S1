# Name:        ProjetHackathon_B2_Grp3
# Purpose:     création d’un carnet d'adresses avec Python et SQLite.
#              
# Author:      Alexandre PUISEUX - alexandre.puiseux@edu.ece.fr
#              Joan-Baptiste FERRANDO - joanbaptiste.ferrando@edu.ece.fr
# Lib : 

import sqlite3
import base64
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import simpledialog
import io

### --------------------------------------------------------- ###

# Création de la base de donné #
with sqlite3.connect("contact.db") as connection:
    cursor = connection.cursor()

def create_bdd():
    cursor.execute(
        "CREATE TABLE contact (id INTEGER PRIMARY KEY AUTOINCREMENT,nomComplet TEXT, genre TEXT,  email TEXT, telephone INTEGER, adresse TEXT, pays TEXT, imageID BLOB)")
    connection.commit()

# Liste des Actions
#--# Ajout Contact #--#
class FenetreAjoutContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ajouter un contact")

        self.label_nom = tk.Label(self, text="Nom Complet:")
        self.entry_nom = tk.Entry(self)

        self.label_genre = tk.Label(self, text="Genre:")
        self.entry_genre = tk.Entry(self)

        self.label_email = tk.Label(self, text="Email:")
        self.entry_email = tk.Entry(self)

        self.label_telephone = tk.Label(self, text="Téléphone:")
        self.entry_telephone = tk.Entry(self)

        self.label_adresse = tk.Label(self, text="Adresse:")
        self.entry_adresse = tk.Entry(self)

        self.label_pays = tk.Label(self, text="Pays:")
        self.entry_pays = tk.Entry(self)

        self.label_imageID = tk.Label(self, text="Image ID:")
        self.entry_imageID = tk.Entry(self)

        self.button_ajouter = tk.Button(self, text="Ajouter", command=self.ajouter_contact)

        self.label_nom.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nom.grid(row=0, column=1, padx=5, pady=5)

        self.label_genre.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_genre.grid(row=1, column=1, padx=5, pady=5)

        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_telephone.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_telephone.grid(row=3, column=1, padx=5, pady=5)

        self.label_adresse.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_adresse.grid(row=4, column=1, padx=5, pady=5)

        self.label_pays.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_pays.grid(row=5, column=1, padx=5, pady=5)

        self.button_ajouter.grid(row=7, column=0, columnspan=2, pady=10)

    def ajouter_contact(self):
        nomComplet = self.entry_nom.get()
        genre = self.entry_genre.get()
        email = self.entry_email.get()
        telephone = self.entry_telephone.get()
        adresse = self.entry_adresse.get()
        pays = self.entry_pays.get()
        imageID = self.ImageAjout()

        with sqlite3.connect("contact.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO contact (nomComplet, genre, email, telephone, adresse, pays, imageID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nomComplet, genre, email, telephone, adresse, pays, imageID)
            )
            connection.commit()
        self.destroy()

    def ImageAjout(self):
        fenetreImage = tk.Toplevel(self)
        fenetreImage.geometry("700x300+500+300")

        remplir = tk.IntVar()  
        texte = tk.Label(fenetreImage, text="Voulez-vous choisir votre image ?")
        texte.place(x=20, y=5)
        def bouton1():
            nonlocal remplir  
            remplir = 1
            fenetreImage.destroy()  
            print("\nChoose")

        def bouton2():
            nonlocal remplir
            remplir = 2
            fenetreImage.destroy()
            print("\nDefault")

        bouton1 = tk.Button(fenetreImage, text="Oui", command=bouton1)
        bouton1.place(x=30, y=40)

        bouton2 = tk.Button(fenetreImage, text="Non (Image par défaut)", command=bouton2)
        bouton2.place(x=120, y=40)

        fenetreImage.wait_window(fenetreImage)  

        tampon = ""
        if remplir == 1:
            tampon = tk.filedialog.askopenfilename()
            print("\nremplissage fichier reussi")
        elif remplir == 2:
            tampon = "img/default.png"
            print("\nremplissage défaut reussi")

        if tampon:
            with open(tampon, 'rb') as file:
                imageDonnee = base64.b64encode(file.read()).decode('utf-8')
                print("\nencodage reussi")
                return imageDonnee
        else:
            return None

#--# Afficher Liste Contacts #--# 
class FenetreAfficherListeContacts(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Afficher la liste des contacts")

        with sqlite3.connect("contact.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM contact")
            resultats = cursor.fetchall()

            tableau = ttk.Treeview(self, columns=list(range(len(resultats[0]))), show="headings", height=10)

            for i, header in enumerate(cursor.description):
                tableau.heading(i, text=header[0])
                tableau.column(i, width=100)  

            for row in resultats:
                tableau.insert("", "end", values=row)

            tableau.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

#--# Afficher Rechercher Contacts #--# 
class FenetreRechercherContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rechercher un contact")

        self.label_nom = tk.Label(self, text="Nom Complet:")
        self.entry_nom = tk.Entry(self)
        self.label_nom.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nom.grid(row=0, column=1, padx=5, pady=5)

        self.button_rechercher = tk.Button(self, text="Rechercher", command=self.rechercher_contact)
        self.button_rechercher.grid(row=1, column=0, columnspan=2, pady=10)

    def rechercher_contact(self):
        nomComplet = self.entry_nom.get()

        with sqlite3.connect("contact.db") as connection:
            cursor = connection.cursor()
            try:
                row = cursor.execute(f"SELECT * FROM contact WHERE nomComplet = ?", (nomComplet,)).fetchone()
                if row:
                    messagebox.showinfo("valid", f"Le contact {nomComplet} existe. ")
                    self.afficher_contact(nomComplet)
                    return nomComplet
                else:
                    messagebox.showerror()
            except Exception as e:
                print(f"Erreur {e}")

    def afficher_contact(self, contact):
        fenetre_afficher_contact = tk.Toplevel(self)
        fenetre_afficher_contact.title(f"Afficher le contact - {contact}")
        cursor.execute("SELECT * FROM contact WHERE nomComplet = ?", (contact,))
        resultat = cursor.fetchone()

        labels = ['ID', 'Nom Complet', 'Genre', 'Email', 'Téléphone', 'Adresse', 'Pays']
        for i, label_text in enumerate(labels):
            ttk.Label(fenetre_afficher_contact, text=label_text, background="#FF6F61").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            ttk.Label(fenetre_afficher_contact, text=resultat[i], background="#FF6F61").grid(row=i, column=1, padx=10, pady=5, sticky="w")
        cursor.execute("""
            SELECT imageID
            FROM contact
            WHERE nomComplet = ?
        """, (contact,))
        image_data = cursor.fetchone()[0]
        image_bytes = base64.b64decode(image_data)
        img = plt.imread(io.BytesIO(image_bytes))
        figure, axe = plt.subplots(figsize=(1, 1))
        axe.imshow(img)
        axe.axis("off")
        canvas = FigureCanvasTkAgg(figure, master= fenetre_afficher_contact)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=220, y=10)

#--# Afficher Modifier Contacts #--# 
class FenetreModifierContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Modifier un contact")

        self.label_nom = tk.Label(self, text="Nom Complet:")
        self.entry_nom = tk.Entry(self)
        self.label_nom.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nom.grid(row=0, column=1, padx=5, pady=5)

        self.button_rechercher = tk.Button(self, text="Rechercher", command=self.rechercher_contact)
        self.button_rechercher.grid(row=1, column=0, columnspan=2, pady=10)

    def rechercher_contact(self):
        nomComplet = self.entry_nom.get()
        with sqlite3.connect("contact.db") as connection:
            cursor = connection.cursor()
            try:
                row = cursor.execute(f"SELECT * FROM contact WHERE nomComplet = ?", (nomComplet,)).fetchone()
                if row:
                    messagebox.showinfo("valid", f"Le contact {nomComplet} existe. ")
                    self.modifier_contacte(nomComplet)
                else:
                    messagebox.showerror("Erreur", f"Le contact {nomComplet} n'existe pas.")
            except Exception as e:
                print(f"Erreur {e}")

    def modifier_contacte(self, nomComplet):
        if nomComplet:
            fenetreModif = tk.Toplevel(self)
            fenetreModif.geometry("200x250+350+200")
            boutons_choix = [("Nom Complet", "nomComplet"),
                             ("Email", "email"),
                             ("Téléphone", "telephone"),
                             ("Adresse", "adresse"),
                             ("Pays", "pays"),
                             ("Image ID", "imageID")]

            for nom, colonne in boutons_choix:
                tk.Button(fenetreModif, text=nom, command=lambda c=colonne: self.modif_test(c)).pack()

            tk.Button(fenetreModif, text="Quitter", command=fenetreModif.destroy).pack()

    def modif_test(self, colonne):
        nouvelle_valeur = simpledialog.askstring("Modifier", f"Entrez la nouvelle valeur pour {colonne}:")
        if nouvelle_valeur is not None:
            try:
                query = f"UPDATE contact SET {colonne} = ? WHERE nomComplet = ?"
                values = (nouvelle_valeur, self.entry_nom.get())
                cursor.execute(query, values)
                connection.commit()
                print("Modification réussie.")
            except Exception as e:
                print(f"Une erreur s'est produite : {e}")

#--# Afficher Supprimer Contacts #--# 
class FenetreSupprimerContact(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Supprimer un contact")

        self.label_nom = tk.Label(self, text="Nom Complet:")
        self.entry_nom = tk.Entry(self)
        self.label_nom.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nom.grid(row=0, column=1, padx=5, pady=5)

        self.button_rechercher = tk.Button(self, text="Rechercher", command=self.rechercher_contact)
        self.button_rechercher.grid(row=1, column=0, columnspan=2, pady=10)

    def rechercher_contact(self):
        nomComplet = self.entry_nom.get()
        with sqlite3.connect("contact.db") as connection:
            cursor = connection.cursor()
            try:
                row = cursor.execute(f"SELECT * FROM contact WHERE nomComplet = ?", (nomComplet,)).fetchone()
                if row:
                    messagebox.showinfo("Valid", f"Le contact {nomComplet} existe. ")
                    confirmation = messagebox.askyesno("Confirmation", f"Voulez-vous vraiment supprimer le contact {nomComplet}?")
                    if confirmation:
                        self.supprimer_contact(nomComplet)
                else:
                    messagebox.showerror("Erreur", f"Le contact {nomComplet} n'existe pas.")
            except Exception as e:
                print(f"Erreur {e}")

    def supprimer_contact(self, nomComplet):
        try:
            with sqlite3.connect("contact.db") as connection:
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM contact WHERE nomComplet = ?", (nomComplet,))
                connection.commit()
                messagebox.showinfo("Succès", f"Le contact {nomComplet} a été supprimé avec succès.")
                self.destroy() 
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.expression = tk.StringVar()
        self.expression.set("")
        self.tmp = None

        buttons = [
            'Ajouter un contact',
            'Afficher la liste des contacts',
            'Afficher un contact',
            'Supprimer un contact',
            'Modifier un contact',
            'Rechercher un contact',
            'Quitter'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, width=20, height=2, command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.geometry("900x125")
        self.title("Gestion des contacts")

    def button_click(self, value):
        if value == 'Ajouter un contact':
            print("Ajouter un contact")
            FenetreAjoutContact(self)
        elif value == 'Afficher la liste des contacts':
            print("Afficher la liste des contacts")
            FenetreAfficherListeContacts(self)
        elif value == 'Afficher un contact':
            print("Afficher un contact")
            FenetreRechercherContact(self)
        elif value == 'Supprimer un contact':
            print("Supprimer un contact")
            FenetreSupprimerContact(self)
        elif value == 'Modifier un contact':
            print("Modifier un contact")
            FenetreModifierContact(self)
        elif value == 'Rechercher un contact':
            print("Rechercher un contact")
            FenetreRechercherContact(self)
        else:
            print("Quitter")
            self.destroy() 

if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()
