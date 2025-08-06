from fahrzeug import Fahrzeug

class LKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis, ladegewicht=0):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.ladegewicht = ladegewicht

    def starten(self):
        print(f"{self.marke} {self.modell} startet mit Druckluftsystem.")

    def wechsle_reifen(self):
        print(f"Beim LKW werden {self.anzahl_reifen} Reifen mit Spezialwerkzeug gewechselt.")

    def ladung_aufnehmen(self, gewicht):
        self.ladegewicht += gewicht
        print(f"LKW hat nun {self.ladegewicht} kg Ladung aufgenommen.")