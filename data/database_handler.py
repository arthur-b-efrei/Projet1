import os
import sqlite3

class DatabaseHandler():
    def __init__(self,database_name : str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def get_stock_sum(self):
        cursor = self.con.cursor()
        query = "SELECT SUM(nb) AS total FROM produit;"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result['total']
    

    def get_vente_count(self):
        cursor = self.con.cursor()
        query = "SELECT COUNT(DISTINCT id_v) AS count FROM vente;"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result['count']
    

    def list_vente(self) ->list:
        cursor = self.con.cursor()
        query = f"SELECT * FROM vente;"
        cursor.execute(query)
        result = cursor.fetchall()
        parsed_data = []
        for row in result:
            parsed_data.append({
                "id_v": row["id_v"],
                "id_p": row["id_p"],
                "nb": row["nb"]
            })
        return parsed_data

    def list_produit(self) -> list:
        cursor = self.con.cursor()
        query = f"SELECT * FROM produit;"
        cursor.execute(query)
        result = cursor.fetchall()
        parsed_data = []
        for row in result:
            parsed_data.append({
                "id_p": row["id_p"],
                "id_f": row["id_f"],
                "nom": row["nom"],
                "nb": row["nb"],
                "prix": row["prix"]
            })
        return parsed_data

    def list_fournisseur(self) -> list:
        cursor = self.con.cursor()
        query = f"SELECT * FROM fournisseur;"
        cursor.execute(query)
        result = cursor.fetchall()
        parsed_data = []
        for row in result:
            parsed_data.append({
                "id_f": row["id_f"],
                "nom": row["nom"],
            })
        return parsed_data

    def create_produit(self, id_f: int, nom: str, nb: int, prix: float):
        cursor = self.con.cursor()
        query = f"INSERT INTO produit (id_f,nom,nb,prix) VALUES(?,?,?,?);"
        cursor.execute(query,(id_f,nom,nb,prix))
        cursor.close()
        self.con.commit()

    def create_vente(self, id_p: int, nb: int):
        cursor = self.con.cursor()
        query = f"INSERT INTO vente (id_p,nb) VALUES(?,?);"
        cursor.execute(query,(id_p,nb))
        cursor.close()
        self.con.commit()

    def delete_produit(self, id_p: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM produit WHERE id_p = ?;"
        cursor.execute(query, (id_p,))
        cursor.close()
        self.con.commit()

    def create_fournisseur(self, nom: str):
        cursor = self.con.cursor()
        query = f"INSERT INTO fournisseur (nom) VALUES(?);"
        cursor.execute(query,(nom,))
        cursor.close()
        self.con.commit()

    def delete_fournisseur(self, id_f: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM fournisseur WHERE id_f = ?"
        cursor.execute(query, (id_f))
        cursor.close()
        self.con.commit()