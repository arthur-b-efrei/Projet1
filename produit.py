from tkinter import *
from raccourcis import *
from data.database_handler import DatabaseHandler

database_handler =  DatabaseHandler("database.db")

def btn_pr(fenetre):
    Ajouter = Button(fenetre,text="Ajouter",font=10,bg="purple4",fg="snow",command=lambda: add_prod(fenetre))
    Ajouter.place(x=1100, y=250)
    Modifier = Button(fenetre,text="Modifier",font=10,bg="purple4",fg="snow")
    Modifier.place(x=1100, y=300)
    Supprime = Button(fenetre,text="Supprimer",font=10,bg="purple4",fg="snow", command=lambda: sup_prod(fenetre))
    Supprime.place(x=1100, y=350)
    exit_btn(fenetre)

def add_prod(fenetre):
    add_prod_popup = Toplevel( bg="purple4")
    add_prod_popup.attributes("-fullscreen",True)
    exit_btn(add_prod_popup)
    affichage(add_prod_popup,"id du fournisseur :", 560,100)
    id_f = Entry(add_prod_popup, bg="purple2",fg="snow",font=10)
    id_f.place(x=750, y=100)
    affichage(add_prod_popup,"nom du produit :",580,200)
    nom_p = Entry(add_prod_popup, bg="purple2",fg="snow", font=10)
    nom_p.place(x=750, y=200)
    affichage(add_prod_popup,"nombre :",640,300)
    nb_p = Entry(add_prod_popup, bg="purple2",fg="snow", font=10)
    nb_p.place(x=750, y=300)
    affichage(add_prod_popup,"prix :",660,400)
    prix_p = Entry(add_prod_popup, bg="purple2",fg="snow", font=10)
    prix_p.place(x=750,y=400)
    valider_p = Button(add_prod_popup,text="VALIDER", bg="purple2",fg="snow", font=10, width=50, command=lambda: (database_handler.create_produit(id_f.get(), nom_p.get(), nb_p.get(),prix_p.get()),add_prod_popup.destroy(),fenetre.destroy()))
    valider_p.place(x=500,y=600)

def sup_prod(fenetre):
    sup_prod_popup = Toplevel( bg="purple4")
    sup_prod_popup.attributes("-fullscreen",True)
    exit_btn(sup_prod_popup)
    affichage(sup_prod_popup,"Id du produit :", 560,100)
    id_p = Entry(sup_prod_popup, bg="purple2",fg="snow",font=10)
    id_p.place(x=750, y=100)
    valider_p = Button(sup_prod_popup,text="VALIDER", bg="purple2",fg="snow", font=10, width=50, command=lambda: (database_handler.delete_produit(id_p.get()),sup_prod_popup.destroy(),fenetre.destroy()))
    valider_p.place(x=500,y=600)
