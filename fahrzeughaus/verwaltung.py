from fahrzeug import Fahrzeug
from typing import List

class FahrzeughausVerwaltung:
    def __init__(self):
        self.fahrzeuge = []

    def fahrzeug_hinzufuegen(self, fahrzeug: Fahrzeug):
        self.fahrzeuge.append(fahrzeug)
        print(f"{fahrzeug.marke} {fahrzeug.modell} wurde hinzugefügt.")

    def fahrzeug_entfernen(self, fahrzeug: Fahrzeug):
        if fahrzeug in self.fahrzeuge:
            self.fahrzeuge.remove(fahrzeug)
            print(f"{fahrzeug.marke} {fahrzeug.modell} wurde entfernt.")
        else:
            print("Fahrzeug nicht gefunden.")

    def zeige_alle_fahrzeuge(self):
        print("Fahrzeuge im Fahrzeughaus:")
        for f in self.fahrzeuge:
            f.zeige_fahrzeug_informationen()