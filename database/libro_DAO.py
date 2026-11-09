from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self):
        """
        Recupera tutti i generi distinti presenti nel database per popolare il menu a tendina.
        """
        generi = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore: Impossibile connettersi al database")
            return []

        # Usiamo DISTINCT per evitare duplicati nel menu a tendina
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere ASC"

        try:
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            for row in cursor:
                generi.append(row[0])  # row[0] contiene la stringa del genere

            cursor.close()
            cnx.close()
            return generi

        except Exception as e:
            print(f"Errore in get_all_generi: {e}")
            if cnx.is_connected():
                cnx.close()
            return []

    def get_libri_by_filtri(self, nome_biblioteca, genere):
        libri = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        query = """
            SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca 
            FROM libro l
            JOIN biblioteca b ON l.id_biblioteca = b.id
            WHERE l.genere = COALESCE(%s, l.genere)
              AND b.nome = COALESCE(%s, b.nome)
            ORDER BY l.titolo ASC
        """

        try:
            cursor = cnx.cursor(dictionary=True, buffered=True)
            cursor.execute(query, (genere, nome_biblioteca))

            for row in cursor:
                libro = Libro(row['id'], row['titolo'], row['autore'], row['genere'], row['anno_pubblicazione'],
                              row['id_biblioteca'])
                libri.append(libro)

            cursor.close()
            cnx.close()
            return libri

        except Exception as e:
            print(f"Errore in get_libri_by_filtri: {e}")
            if cnx.is_connected():
                cnx.close()
            return []