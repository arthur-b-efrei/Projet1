from tkinter import *
from tkinter import scrolledtext
from raccourcis import *
from produit import *
from fournisseur import *
from vente import *
from rapport import *
import tkinter as tk
from data.database_handler import DatabaseHandler
Database_handler = DatabaseHandler("database.db")
#importation de la bibliothèque

window = Tk()
window.attributes('-fullscreen', True)
window.config(bg="purple4")
#plein écran et couleur en fond

#menu_definition
def gui():
    add_btn(window,"Produit", 500,200,menu_produit)
    add_btn(window,"Fournisseur", 500,300,menu_fournisseur)
    add_btn(window,"Vente", 500,400,menu_vente)
    add_btn(window,"Rapport", 500,500, menu_rapport)
    exit_btn(window)
    window.mainloop()

#menu_produit
def menu_produit():
    prod_popup = Toplevel(window,bg="purple2")
    prod_popup.attributes('-fullscreen',True)
    indication = affichage(prod_popup,"ID        Fournisseur         nom         nombre          prix",520,100)
    scroll_text = scrolledtext.ScrolledText(prod_popup, width=60, height=80, bg="purple2", fg="snow", wrap=WORD)
    scroll_text.pack(pady=200, padx=100)
    i = 1
    while i ==1:
        btn_pr(prod_popup)
        data_produit = database_handler.list_produit()
        for i in data_produit:
            button = Button(scroll_text, fg="snow",bg="purple4", width=70, text=f"{i['id_p']}                       {i['id_f']}                      {i['nom']}                      {i['nb']}                      {i['prix']}")
            button.pack(padx=0, pady=5)
            scroll_text.window_create(END, window=button)
            scroll_text.insert(END, '\n')
        scroll_text.configure(state='disabled')

#menu_fournisseur
def menu_fournisseur():
    fournisseur_popup = Toplevel(window,bg="purple2")
    fournisseur_popup.attributes('-fullscreen',True)
    indication = affichage(fournisseur_popup, "ID fournisseur       Nom",520,100)
    scroll_text = scrolledtext.ScrolledText(fournisseur_popup, width=60, height=80, bg="purple2", fg="snow", wrap=WORD)
    scroll_text.pack(pady=200, padx=100)
    i = 1
    while i == 1:
        btn_fr(fournisseur_popup)
        data_fournisseur = database_handler.list_fournisseur()
        for i in data_fournisseur:
            button = Button(scroll_text, fg="snow", bg="purple4", width=70, text=f"{i['id_f']}          {i['nom']}")
            button.pack(padx=0, pady=5)
            scroll_text.window_create(END, window=button)
            scroll_text.insert(END, '\n')
        scroll_text.configure(state='disabled')

#menu_vente
def menu_vente():
    vente_popup = Toplevel(window, bg="purple2")
    vente_popup.attributes('-fullscreen',True)
    indication = affichage(vente_popup,"ID      ID produit      nombre",520,100)
    scroll_text = scrolledtext.ScrolledText(vente_popup,width=60, height=80, bg="purple2", fg="snow", wrap=WORD)
    scroll_text.pack(pady=200, padx=100)
    i = 1
    while i == 1:
        btn_v(vente_popup)
        data_vente = database_handler.list_vente()
        for i in data_vente:
            button = Button(scroll_text, fg="snow", bg="purple4", width=70, text=f"{i['id_v']}                          {i['id_p']}                    {i['nb']}")
            button.pack(padx=0, pady=5)
            scroll_text.window_create(END, window=button)
            scroll_text.insert(END, '\n')
        scroll_text.configure(state='disabled')

#menu_raport
def menu_rapport():
    rapport_popup = Toplevel(window, bg="purple2")
    rapport_popup.attributes('-fullscreen', True)
    indication = affichage(rapport_popup, " STOCK            VENTE",520,100)
    scroll_text = scrolledtext.ScrolledText(rapport_popup,width=60, height=80, bg="purple2", fg="snow", wrap=WORD)
    scroll_text.pack(pady=200, padx=100)
    i= 1
    while i ==1:
        btn_r(rapport_popup)
        data_stock = database_handler.get_stock_sum()
        data_vente = database_handler.get_vente_count()
        for i in range(2):
            button = Button(scroll_text, fg="snow", bg="purple4", width=70, text=f"{i['stock']}          {i['vente']}")
            button.pack(padx=0, pady=5)
            scroll_text.window_create(END, window=button)
            scroll_text.insert(END, '\n')
        scroll_text.configure(state='disabled')


gui()

