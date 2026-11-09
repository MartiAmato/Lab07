import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
- Rappresenta l'interfaccia utente
- Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        self.dd_biblioteca = ft.Dropdown(
            label="Seleziona Biblioteca",
            width=300,
            options=[],
            on_select=self.controller.on_select_biblioteca
        )

        self.dd_genere = ft.Dropdown(
            label="Seleziona Genere",
            width=300,
            options=[],
            on_select=self.controller.on_select_genere
        )

        # --- Sezione 3: Libri ---
        # Sostituiamo ElevatedButton (rimosso in Flet 1.0) con il nuovo Button
        self.btn_mostra_libri = ft.Button(
            content="Mostra Libri",
            on_click=self.controller.mostra_libri
        )

        # La ListView che conterrà gli elementi letti dal DB
        self.lst_libri = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(
                controls=[self.dd_biblioteca, self.dd_genere],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            # Sezione 3: Libri (Mettiamo il bottone in una Row per centrarlo)
            ft.Row(
                controls=[self.btn_mostra_libri],
                alignment=ft.MainAxisAlignment.CENTER
            ),

            # Aggiungiamo la ListView
            self.lst_libri
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

    # --- Metodo di utilità per retrocompatibilità col controller ---
    def update_page(self):
        self.update()

    def crea_alert(self, messaggio):
        self.show_alert(messaggio)