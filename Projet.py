# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:39:43 2024

@author: USER
"""

import tkinter as tk
from tkinter import PhotoImage
import random

# Fonction pour déterminer le gagnant
def jouer(choix_utilisateur):
    choix_ordi = random.choice(['Pierre', 'Papier', 'Ciseaux'])
    
    if choix_utilisateur == choix_ordi:
        result = f"Égalité ! Vous avez choisi {choix_utilisateur} et l'ordinateur a choisi {choix_ordi}."
    elif (choix_utilisateur == 'Pierre' and choix_ordi == 'Ciseaux') or \
         (choix_utilisateur == 'Papier' and choix_ordi == 'Pierre') or \
         (choix_utilisateur == 'Ciseaux' and choix_ordi == 'Papier'):
        result = f"Vous avez gagné ! Vous avez choisi {choix_utilisateur} et l'ordinateur a choisi {choix_ordi}."
    else:
        result = f"Vous avez perdu ! Vous avez choisi {choix_utilisateur} et l'ordinateur a choisi {choix_ordi}."
    
    # Afficher le résultat
    label_resultat.config(text=result)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu Pierre-Papier-Ciseaux")
root.geometry("700x500")

# Ajout d'un titre
label_title = tk.Label(root, text="Jeu Pierre  Papier  Ciseaux", font=("Perpetua", 20))
label_title.pack(pady=15)

# Charger les images

rock_image = PhotoImage(file="C:/Users/USER/Desktop/DARIF 2024/TOP/Cours/Dernier_Projet/images/pierre.png")  
paper_image = PhotoImage(file="C:/Users/USER/Desktop/DARIF 2024/TOP/Cours/Dernier_Projet/images/papier.png")  
scissors_image = PhotoImage(file="C:/Users/USER/Desktop/DARIF 2024/TOP/Cours/Dernier_Projet/images/ciseaux.png") 

# Ajout des boutons pour chaque choix avec des images
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

button_pierre = tk.Button(frame_buttons, image=rock_image, command=lambda: jouer('Pierre'))
button_pierre.grid(row=0, column=0, padx=10)

button_papier = tk.Button(frame_buttons, image=paper_image, command=lambda: jouer('Papier'))
button_papier.grid(row=0, column=1, padx=10)

button_ciseaux = tk.Button(frame_buttons, image=scissors_image, command=lambda: jouer('Ciseaux'))
button_ciseaux.grid(row=0, column=2, padx=10)

button_quitter = tk.Button(frame_buttons, text="Quitter", command=root.destroy).grid(column=1, row=1, pady=20)

# Label pour afficher le résultat
label_resultat = tk.Label(root, text="", font=("Helvetica", 12), wraplength=300)
label_resultat.pack(pady=20)

# Démarrage de la boucle principale
root.mainloop()