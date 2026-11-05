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
    def popola_dropdownBiblioteche(self):
        biblioteche = self._model.get_biblioteche() #recupero tutte le biblioteche dal model
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for biblioteca in biblioteche:
           self._view.dd_biblioteca.options.append(ft.dropdown.Option(f"{biblioteca.nome}"))

        self._view.update()

    def popola_dropdownGenere(self):
        generi = self._model.get_generi()  # recupero tutte i dati dal model
        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(f"{genere}"))

        self._view.update()

    # CALLBACKS DROPDOWN
    # Funzione richiamata automaticamente da flet quando l'utente compie un'azione (es. seleziona una voce nel dropdown)
    # Serve a intercettare l'evento (e), leggere la scelta e salvarla nelle variabili del controller.
    def handler_selezionaBiblioteca(self, e):
        self.biblioteca_selezionata = e.control.value #prende il valore selezionato dall'utente

    def handler_selezionaGenere(self, e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def handler_libri(self, e):
        #recupero i dati tramite il model
        libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        #svuoto la lista visiva nella view dai risultati precedenti
        self._view.list_view.controls.clear()

        # mi assicuro che esistano dei libri e li aggiungo alla list view
        if not libri_filtrati:
            self._view.list_view.controls.append(ft.Text("Nessun libro trovato con i filtri selezionati."))
        else:
            for libro in libri_filtrati:
                self._view.list_view.controls.append(ft.Text(f"{libro}"))
        self._view.update()




