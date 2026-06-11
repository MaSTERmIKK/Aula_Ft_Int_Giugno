# Classe che rappresenta un singolo piatto del menu
class Piatto:

    # Costruttore della classe Piatto
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    # Metodo che descrive il piatto
    def descrivi_piatto(self):
        print(f"Piatto: {self.nome} - Prezzo: {self.prezzo} euro")


# Classe che rappresenta un ristorante
class Ristorante:

    # Costruttore della classe Ristorante
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = []

    # Metodo che descrive il ristorante
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre cucina {self.tipo_cucina}.")

    # Metodo che stampa lo stato del ristorante
    def stato_apertura(self):
        if self.aperto == True:
            print("Il ristorante è aperto.")
        else:
            print("Il ristorante è chiuso.")

    # Metodo per aprire il ristorante
    def apri_ristorante(self):
        self.aperto = True
        print(f"{self.nome} è ora aperto.")

    # Metodo per chiudere il ristorante
    def chiudi_ristorante(self):
        self.aperto = False
        print(f"{self.nome} è ora chiuso.")

    # Metodo per aggiungere un piatto al menu
    def aggiungi_al_menu(self, piatto):
        self.menu.append(piatto)
        print(f"{piatto.nome} è stato aggiunto al menu.")

    # Metodo per togliere un piatto dal menu
    def togli_dal_menu(self, nome_piatto):
        trovato = False

        for piatto in self.menu:
            if piatto.nome == nome_piatto:
                self.menu.remove(piatto)
                trovato = True
                print(f"{nome_piatto} è stato rimosso dal menu.")
                break

        if trovato == False:
            print(f"{nome_piatto} non è presente nel menu.")

    # Metodo per stampare tutto il menu
    def stampa_menu(self):
        print(f"\nMenu del ristorante {self.nome}:")

        if len(self.menu) == 0:
            print("Il menu è vuoto.")
        else:
            for piatto in self.menu:
                piatto.descrivi_piatto()


# -------------------------
# TEST DEL PROGRAMMA
# -------------------------

# Creo alcuni oggetti Piatto
piatto1 = Piatto("Pizza Margherita", 7.50)
piatto2 = Piatto("Pasta alla Carbonara", 10.00)
piatto3 = Piatto("Tiramisù", 5.00)

# Creo un oggetto Ristorante
ristorante = Ristorante("Da Mario", "italiana")

# Test dei metodi del ristorante
ristorante.descrivi_ristorante()
ristorante.stato_apertura()

ristorante.apri_ristorante()
ristorante.stato_apertura()

# Aggiungo piatti al menu
ristorante.aggiungi_al_menu(piatto1)
ristorante.aggiungi_al_menu(piatto2)
ristorante.aggiungi_al_menu(piatto3)

# Stampo il menu
ristorante.stampa_menu()

# Tolgo un piatto dal menu
ristorante.togli_dal_menu("Tiramisù")

# Ristampo il menu aggiornato
ristorante.stampa_menu()

# Chiudo il ristorante
ristorante.chiudi_ristorante()
ristorante.stato_apertura()
