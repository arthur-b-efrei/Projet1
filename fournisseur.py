from tkinter import *
from raccourcis import *
from data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def btn_fr(fenetre):
    Ajouter = Button(fenetre,text="Ajouter",font=10,bg="purple4",fg="snow",command=lambda: add_fr(fenetre))
    Ajouter.place(x=1100, y=250)
    Modifier = Button(fenetre,text="Modifier",font=10,bg="purple4",fg="snow")
    Modifier.place(x=1100, y=300)
    Supprime = Button(fenetre,text="Supprimer",font=10,bg="purple4",fg="snow", command=lambda: sup_fr(fenetre))
    Supprime.place(x=1100, y=350)
    exit_btn(fenetre)

def add_fr(fenetre):
    add_fr_popup = Toplevel(bg="purple4")
    add_fr_popup.attributes("-fullscreen", True)
    exit_btn(add_fr_popup)
    affichage(add_fr_popup,"nom :",580,100)
    nom_f = Entry(add_fr_popup, bg="purple2",fg="snow", font=10)
    nom_f.place(x=750,y=400)
    valider_p = Button(add_fr_popup,text="VALIDER", bg="purple2",fg="snow", font=10, width=50, command=lambda: (database_handler.create_fournisseur(nom_f.get()),fenetre.destroy(),add_fr_popup.destroy()))
    valider_p.place(x=500,y=600)

def sup_fr(fenetre):
    sup_fr_popup = Toplevel( bg="purple4")
    sup_fr_popup.attributes("-fullscreen",True)
    exit_btn(sup_fr_popup)
    affichage(sup_fr_popup,"Id du fournisseur :", 560,100)
    id_f = Entry(sup_fr_popup, bg="purple2",fg="snow",font=10)
    id_f.place(x=750, y=100)
    valider_p = Button(sup_fr_popup,text="VALIDER", bg="purple2",fg="snow", font=10, width=50, command=lambda: (database_handler.delete_fournisseur(id_f.get()),fenetre.destroy(),sup_fr_popup.destroy()))
    valider_p.place(x=500,y=600)