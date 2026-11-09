from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
- Rappresenta la struttura dati
- Si occupa di gestire lo stato dell'applicazione
- Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca: str, genere: str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # Passiamo le stringhe dei filtri direttamente al DAO.
        # Se il valore è "None", il DAO saprà che quel filtro non è attivo.
        return self._libro_dao.get_libri_by_filtri(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # Chiamiamo il metodo del DAO che esegue una query del tipo:
        # "SELECT DISTINCT genere FROM libro"
        return self._libro_dao.get_all_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # Chiamiamo il metodo del DAO per ottenere la lista di tutti
        # gli oggetti di tipo Biblioteca (o le relative stringhe)
        return self._biblioteca_dao.get_all()

    # --- METODI ALIAS (per retrocompatibilità col Controller) ---
    def get_all_biblioteche(self):
        return self.get_biblioteche()

    def get_all_generi(self):
        return self.get_generi()
