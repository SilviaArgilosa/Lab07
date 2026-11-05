from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_libri(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = f"""SELECT * FROM libro"""
        cursor.execute(query)

        libri = []
        for riga in cursor:
            libro = Libro(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
            libri.append(libro)

        cursor.close()
        conn.close()
        return libri

    def prendi_generi(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()
        query = f"""SELECT DISTINCT `genere` FROM libro"""
        cursor.execute(query)

        generi = []
        for genere in cursor:
            generi.append(genere[0])

        cursor.close()
        conn.close()
        return generi

    def filtra_libri(self, nome_biblioteca, genere):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        #divido i vari casi
        #caso 1: genere e biblioteca sono stati selezionati
        if nome_biblioteca is not None and nome_biblioteca != "Nessun filtro" and genere is not None and genere != "Nessun filtro":
            query =f"""SELECT * FROM libro 
                       WHERE genere = '{genere}' AND 
                       id_biblioteca = (SELECT id FROM biblioteca WHERE nome = '{nome_biblioteca}')"""

        #caso 2: solo biblioteca è stata selezionata
        elif nome_biblioteca is not None and nome_biblioteca != "Nessun filtro":
            query = f"""SELECT * FROM libro 
                                   WHERE id_biblioteca = (SELECT id FROM biblioteca WHERE nome = '{nome_biblioteca}')"""

        #caso 3: solo genere è stato selezionato
        elif genere is not None and genere != "Nessun filtro":
            query = f"""SELECT * FROM libro 
                                   WHERE genere = '{genere}' 
                     """

        #caso 4: nessun parametro è stato scelto
        else:
            query = f"""SELECT * FROM libro """


        cursor.execute(query)

        libri = []
        for riga in cursor:
            libro = Libro(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
            libri.append(libro)

        cursor.close()
        conn.close()
        return libri


