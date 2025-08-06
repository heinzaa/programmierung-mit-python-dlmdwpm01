from fahrzeug import Fahrzeug

class PKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis, kofferraumvolumen=400):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.kofferraumvolumen = kofferraumvolumen
        self.kofferraum_offen = False

    def starten(self):
        print(f"{self.marke} {self.modell} startet den Motor.")

    def wechsle_reifen(self):
        print(f"Beim PKW werden alle {self.anzahl_reifen} Reifen in der Werkstatt gewechselt.")

    def kofferraum_oeffnen(self):
        self.kofferraum_offen = True
        print("Der Kofferraum ist jetzt geöffnet.")

    def kofferraum_schliessen(self):
        self.kofferraum_offen = False
        print("Der Kofferraum ist jetzt geschlossen.")