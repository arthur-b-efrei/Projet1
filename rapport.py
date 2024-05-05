from tkinter import *
from raccourcis import *
from data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def btn_r(fenetre):
    exit_btn(fenetre)