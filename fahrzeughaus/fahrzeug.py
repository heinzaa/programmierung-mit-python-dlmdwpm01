from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    def __init__(self, marke: str, modell: str, baujahr: int, anzahl_reifen: int, preis: float):
        self.__marke = marke
        self.__modell = modell
        self.__baujahr = baujahr
        self.__anzahl_reifen = anzahl_reifen
        self.__preis = preis

    # Getter
    @property
    def marke(self):
        return self.__marke

    @property
    def modell(self):
        return self.__modell

    @property
    def baujahr(self):
        return self.__baujahr

    @property
    def anzahl_reifen(self):
        return self.__anzahl_reifen

    @property
    def preis(self):
        return self.__preis

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
        self.__preis *= (1 - prozent / 100)

    # Verhalten
    @abstractmethod
    def starten(self):
        pass

    def zeige_fahrzeug_informationen(self):
        print(f"{self.__marke} {self.__modell}, Baujahr {self.__baujahr}, {self.__anzahl_reifen} Reifen, Preis: {self.__preis}€")

    def wechsle_reifen(self):
        print(f"Es werden {self.__anzahl_reifen} Reifen gewechselt.")