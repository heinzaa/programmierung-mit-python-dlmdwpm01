from fahrzeug import Fahrzeug

class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, anzahl_reifen, preis):
        super().__init__(marke, modell, baujahr, anzahl_reifen, preis)
        self.sitzbank_geoeffnet = False
        self.staender_eingeklappt = False

    @property
    def staender_eingeklappt(self):
        return self._staender_eingeklappt

    @staender_eingeklappt.setter
    def staender_eingeklappt(self, wert: bool):
        if not isinstance(wert, bool):
            raise ValueError("Ständerstatus muss ein boolescher Wert sein.")
        self._staender_eingeklappt = wert
        aktion = "eingeklappt" if wert else "ausgeklappt"
        print(f"Ständer {aktion}.")
    
    def starten(self):
        if not self.staender_eingeklappt:
            print(f"Kann {self.marke} {self.modell} nicht starten: "
                  f"Bitte Ständer einklappen.")
        else:
            print(f"{self.marke} {self.modell} Motor durch Knopfdruck gestartet.")

    def wechsle_reifen(self):
        print(f"Beim Motorrad werden {self.anzahl_reifen} Reifen von Hand gewechselt.")

    def sitzbank_oeffnen(self):
        self.sitzbank_geoeffnet = True
        print(f"Die Sitzbank ist jetzt geöffnet für {self.marke} {self.modell}.")

    def sitzbank_schliessen(self):
        self.sitzbank_geoeffnet = False
        print(f"Die Sitzbank ist jetzt geschlossen für {self.marke} {self.modell}.")

    