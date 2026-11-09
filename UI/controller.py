import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
- Funziona da intermediario tra MODELLO e VIEW
- Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdowns(self):

        self._view.dd_biblioteca.options.clear()
        self._view.dd_genere.options.clear()

        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))

        biblioteche = self._model.get_all_biblioteche()
        for b in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(b.nome))


        generi = self._model.get_all_generi()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(g))


        self._view.update_page()

    # CALLBACKS DROPDOWN
    def on_select_biblioteca(self, e):
        valore = self._view.dd_biblioteca.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def on_select_genere(self, e):
        valore = self._view.dd_genere.value
        if valore == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        self._view.lst_libri.controls.clear()


        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)


        if not libri:
             self._view.crea_alert("Nessun libro trovato per i filtri selezionati!")
        else:
            for libro in libri:
                self._view.lst_libri.controls.append(ft.Text(str(libro)))

        self._view.update_page()