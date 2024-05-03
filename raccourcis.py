from tkinter import *
from tkinter import scrolledtext

def add_btn(fenetre, string, X, Y, Command=None):
    btn = Button(fenetre,text=string,fg="snow", bg="purple2",width=50,font=10, command=Command)
    btn.place(x=X, y=Y)

def affichage(fenetre,string,X,Y):
    S = Label(fenetre, text=string, fg="snow", bg="purple2",font=10)
    S.place(x=X,y=Y)

def exit_btn(fenetre):
    exit = Button(fenetre, text="Quitter", font=10,command=fenetre.destroy, bg="red",fg="snow", width=50)
    exit.place(x=500, y=700)