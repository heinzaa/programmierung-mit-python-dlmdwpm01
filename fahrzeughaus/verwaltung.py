from fahrzeug import Fahrzeug
from typing import List

class FahrzeughausVerwaltung:
    def __init__(self):
        self._fahrzeuge: List[Fahrzeug] = []
        
    @property
    def fahrzeuge(self)-> List[Fahrzeug]:
        return list(self._fahrzeuge)
    
    #Fahrzeug hinzufügen
    def fahrzeug_hinzufuegen(self, fahrzeug: Fahrzeug):
        if fahrzeug not in self._fahrzeuge:
            self._fahrzeuge.append(fahrzeug)
            print(f"{fahrzeug.marke} {fahrzeug.modell} wurde hinzugefügt.")
        else:
            print(f"Fahrzeug {fahrzeug.marke} {fahrzeug.modell} ist bereits vorhanden.")
            
    def fahrzeug_entfernen(self, fahrzeug: Fahrzeug):
        if fahrzeug in self._fahrzeuge:
            self._fahrzeuge.remove(fahrzeug)
            print(f"Fahrzeug {fahrzeug.marke} {fahrzeug.modell} wurde entfernt.")
        else:
            print("Fahrzeug nicht gefunden.")

    # Alle Fahrzeuge anzeigen
    def zeige_alle_fahrzeuge(self):
        if not self._fahrzeuge:
            print("Keine Fahrzeuge im Bestand.")
            return
        print("\n--- Fahrzeugbestand ---")
        for fahrzeug in self._fahrzeuge:
            fahrzeug.zeige_fahrzeug_informationen()