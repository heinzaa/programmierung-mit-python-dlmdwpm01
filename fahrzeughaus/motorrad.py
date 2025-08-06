from fahrzeug import Fahrzeug

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.sitzbank_geoeffnet = False

    def starten(self):
        print(f"{self.marke} {self.modell} startet mit einem Knopfdruck.")

    def wechsle_reifen(self):
        print(f"Beim Motorrad werden {self.anzahl_reifen} Reifen von Hand gewechselt.")

    def sitzbank_oeffnen(self):
        self.sitzbank_geoeffnet = True
        print("Die Sitzbank ist jetzt geöffnet.")

    def sitzbank_schliessen(self):
        self.sitzbank_geoeffnet = False
        print("Die Sitzbank ist jetzt geschlossen.")