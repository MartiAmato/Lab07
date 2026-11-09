from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""


class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all(self):
        biblioteche = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        query = "SELECT id, nome, indirizzo FROM biblioteca ORDER BY nome ASC"

        try:
            cursor = cnx.cursor(dictionary=True, buffered=True)
            cursor.execute(query)

            for row in cursor:
                # Passiamo tutti e 3 i parametri al DTO
                biblioteca = Biblioteca(row['id'], row['nome'], row['indirizzo'])
                biblioteche.append(biblioteca)

            cursor.close()
            cnx.close()
            return biblioteche

        except Exception as e:
            print(f"Errore in get_all di BibliotecaDAO: {e}")
            if cnx.is_connected():
                cnx.close()
            return []