from fahrzeug import Fahrzeug

class LKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis, ladegewicht=0):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.ladegewicht = ladegewicht

    def starten(self):
        print(f"{self.marke} {self.modell} startet seinen Motor.")

    def wechsle_reifen(self):
        print(f"Beim {self.marke} {self.modell} werden {self.anzahl_reifen} Reifen mit Spezialwerkzeug in einer großen Werkstatt gewechselt.")

    def ladung_aufnehmen(self, gewicht):
        self.ladegewicht += gewicht
        print(f"{self.marke} {self.modell} hat nun {self.ladegewicht} Kilogram Ladung aufgenommen.")