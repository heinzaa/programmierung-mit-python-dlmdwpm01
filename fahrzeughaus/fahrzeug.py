from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    def __init__(self, marke: str, modell: str, baujahr: int, anzahl_reifen: int, preis: float):
        self._marke = marke
        self._modell = modell
        self._baujahr = baujahr
        self._anzahl_reifen = anzahl_reifen
        self._preis = preis

    # Getter
    @property
    def marke(self):
        return self._marke

    @property
    def modell(self):
        return self._modell

    @property
    def baujahr(self):
        return self._baujahr

    @property
    def anzahl_reifen(self):
        return self._anzahl_reifen

    @property
    def preis(self):
        return self._preis

    # Setter mit Validierung
    @preis.setter
    def preis(self, wert):
        if wert < 0:
            raise ValueError("Preis darf nicht negativ sein.")
        self._preis = wert

    # Rabattmethode
    def setze_rabatt(self, prozent: float):
        if not 0 <= prozent <= 100:
            raise ValueError("Rabatt muss zwischen 0 und 100 liegen.")
        self._preis *= (1 - prozent / 100)

    # Verhalten
    @abstractmethod
    def starten(self):
        pass

    def zeige_fahrzeug_informationen(self):
        print(f"{self._marke} {self._modell}, Baujahr {self._baujahr}, {self._anzahl_reifen} Reifen, Preis: {self._preis}€")

    def wechsle_reifen(self):
        print(f"Es werden {self._anzahl_reifen} Reifen gewechselt.")