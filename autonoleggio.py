class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.responsabile=responsabile
        self.automobili = []    # lista di oggetti Automobile
        self.noleggi = []       # lista di oggetti Noleggio

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        # TODO
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for riga in f:
                    codice, marca, modello, anno, num_posti = riga.strip().split(',')
                    anno = int(anno)
                    num_posti = int(num_posti)

                    auto = Automobile(codice, marca, modello, anno, num_posti)
                    self.automobili.append(auto)

        except FileNotFoundError:
            return None


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if not self.automobili:
            nuovo_codice = "A1"
        else:
            ultimo_codice = max(int(a.codice[1:]) for a in self.automobili)
            nuovo_codice = f"A{ultimo_codice + 1}"

        nuova_auto = Automobile(nuovo_codice, marca, modello, anno, num_posti)
        self.automobili.append(nuova_auto)
        return nuova_auto

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO
        return sorted(self.automobili, key=lambda a: a.marca.lower())

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO
        auto = None
        for a in self.automobili:
            if a.codice == id_automobile:
                auto = a
                break

        if auto is None:
            raise Exception("Errore: automobile non trovata nel sistema.")

        if auto.noleggiata:
            raise Exception("Errore: automobile già noleggiata.")

        if not self.noleggi:
            codice_noleggio = "N1"
        else:
            ultimo = max(int(n.codice[1:]) for n in self.noleggi)
            codice_noleggio = f"N{ultimo + 1}"

        noleggio = Noleggio(codice_noleggio, data, id_automobile, cognome_cliente)
        self.noleggi.append(noleggio)
        auto.noleggiata = True

        return noleggio
    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
        noleggio = None
        for n in self.noleggi:
            if n.codice == id_noleggio:
                noleggio = n
                break
        if not noleggio:
            raise Exception("Errore: noleggio non esistente.")

        auto = None
        for a in self.automobili:
            if a.codice == id_noleggio:
                auto = a
                break
        if auto:
            auto.noleggiata = False

        self.noleggi.remove(noleggio)




class Automobile:
    def __init__(self, codice, marca, modello, anno, num_posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.num_posti = num_posti
        self.noleggiata = False  # indica se è attualmente noleggiata

    def __str__(self):
        stato = "Noleggiata" if self.noleggiata else "Disponibile"
        return f"{self.codice} - {self.marca} {self.modello} ({self.anno}, {self.num_posti} posti) - {stato}"

class Noleggio:
    def __init__(self, codice, data, id_auto, cognome_cliente):
        self.codice = codice
        self.data = data
        self.id_auto = id_auto
        self.cognome_cliente = cognome_cliente

    def __str__(self):
        return f"{self.codice}: Auto {self.id_auto} noleggiata da {self.cognome_cliente} il {self.data}"