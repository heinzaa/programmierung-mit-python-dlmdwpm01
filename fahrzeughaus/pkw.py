from fahrzeug import Fahrzeug

class PKW(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis, kofferraumvolumen=400):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.kofferraumvolumen = kofferraumvolumen
        self.kofferraum_offen = False

    def starten(self):
        print(f"{self.marke} {self.modell} startet den Motor durch einen Schlüssel.")

    def wechsle_reifen(self):
        print(f"Beim {self.marke} {self.modell} werden alle {self.anzahl_reifen} Reifen in der Werkstatt gewechselt.")

    def kofferraum_oeffnen(self):
        self.kofferraum_offen = True
        print(f"Der Kofferraum ist jetzt geöffnet für {self.marke} {self.modell}.")

    def kofferraum_schliessen(self):
        self.kofferraum_offen = False
        print(f"Der Kofferraum ist jetzt geschlossen für {self.marke} {self.modell}.")