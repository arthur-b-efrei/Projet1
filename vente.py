from tkinter import *
from raccourcis import *
from data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def btn_v(fenetre):
    vendre = Button(fenetre,text="Vendre",font=10,bg="purple4",fg="snow",command=lambda: add_vente(fenetre))
    vendre.place(x=1100, y=300)
    exit_btn(fenetre)

def add_vente(fenetre):
    add_vente_popup = Toplevel(bg="purple4")
    add_vente_popup.attributes("-fullscreen", True)
    exit_btn(add_vente_popup)
    affichage(add_vente_popup,"ID du produit :",560,100)
    id_p  = Entry(add_vente_popup, bg="purple4", fg="snow", font=10)
    id_p.pack(padx=750,pady=100)
    affichage(add_vente_popup,"Nombre :",580,200)
    nb = Entry(add_vente_popup, bg="purple4", fg="snow", font=10)
    nb.pack(padx=750,pady=200)
    valider_v = Button(add_vente_popup,text="VALIDER", bg="purple2",fg="snow", font=10, width=50, command=lambda: (database_handler.create_vente(id_p.get(),nb.get()),add_vente_popup.destroy(),fenetre.destroy()))
    valider_v.place(x=500,y=600)
