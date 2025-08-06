from fahrzeug import Fahrzeug

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.sitzbank_geoeffnet = False

    def starten(self):
        print(f"{self.marke} {self.modell} Motor durch einen Knopfdruck gestartet.")

    def wechsle_reifen(self):
        print(f"Beim Motorrad werden {self.anzahl_reifen} Reifen von Hand gewechselt.")

    def sitzbank_oeffnen(self):
        self.sitzbank_geoeffnet = True
        print(f"Die Sitzbank ist jetzt geöffnet für {self.marke} {self.modell}.")

    def sitzbank_schliessen(self):
        self.sitzbank_geoeffnet = False
        print(f"Die Sitzbank ist jetzt geschlossen für {self.marke} {self.modell}.")