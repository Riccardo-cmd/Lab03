class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.automobile = []

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                auto = f.read().strip().splitlines()
                for macchina in auto:
                    codice, marca, modello, anno, num_posti = macchina.strip().split(',')
                    anno = int(anno)
                    num_posti = int(num_posti)
                    self.automobile.append(codice, marca, modello, anno, num_posti)
            return self.automobile
            #return f"codice = {self.codice}, marca = {self.marca}, modello = {self.modello}, anno = {self.anno}, num_posti = {self.num_posti}"

        except FileNotFoundError:
            return None


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        ultimo_codice = len(self.automobile) - 1
        nuovo_codice = f"A{ultimo_codice + 1}"
        self.automobile.append(nuovo_codice, marca, modello, anno, num_posti)


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO




class Automobile:
    def __init__(self, codice, marca, modello, anno, num_posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.num_posti = int(num_posti)
