from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

#recuperare l'elenco di tutte le biblioteche presenti nel database
class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = f"""SELECT * FROM biblioteca"""
        cursor.execute(query)

        biblioteche = []
        for riga in cursor:
            biblioteca = Biblioteca(riga[0], riga[1], riga[2])
            biblioteche.append(biblioteca)

        cursor.close()
        conn.close()
        return biblioteche

