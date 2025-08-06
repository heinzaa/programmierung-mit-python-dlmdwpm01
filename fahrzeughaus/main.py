from pkw import PKW
from motorrad import Motorrad
from lkw import LKW
from verwaltung import FahrzeughausVerwaltung

def main():
    # Instanz der Verwaltungsklasse
    verwaltung = FahrzeughausVerwaltung()

    # Fahrzeuge erzeugen (Konkrete Instanzen)
    pkw_vw = PKW("VW", "Golf", 2020, 4, 20000, kofferraumvolumen=380)
    pkw_bmw = PKW("BMW", "3er", 2021, 4, 25000, kofferraumvolumen=450)
    motorrad_yamaha = Motorrad("Yamaha", "MT-07", 2022, 2, 8000)
    lkw_man = LKW("MAN", "TGX", 2019, 6, 60000, ladegewicht=10000)

    # Kapselung: nur über Methoden steuerbar
    motorrad_yamaha.sitzbank_oeffnen()
    motorrad_yamaha.sitzbank_schliessen()
    lkw_man.ladung_aufnehmen(500)

    # Fahrzeuge zur Verwaltung hinzufügen
    verwaltung.fahrzeug_hinzufuegen(pkw_vw)
    verwaltung.fahrzeug_hinzufuegen(pkw_bmw)
    verwaltung.fahrzeug_hinzufuegen(motorrad_yamaha)
    verwaltung.fahrzeug_hinzufuegen(lkw_man)

    # Ausgabe: alle Fahrzeuge anzeigen
    print("\n--- Fahrzeugbestand ---")
    verwaltung.zeige_alle_fahrzeuge()

    # Polymorphie: Start und Reifenwechsel unabhängig vom konkreten Typ
    print("\n--- Polymorphismus-Demo ---")
    for fahrzeug in verwaltung.fahrzeuge:
        verwaltung.zeige_fahrzeugdetails(fahrzeug)
        verwaltung.fuehre_reifenwechsel_durch(fahrzeug)
        fahrzeug.starten()

    # Gesamtwert berechnen
    print("\n--- Gesamtwert der Fahrzeuge ---")
    print(f"{verwaltung.berechne_gesamtwert():,.2f} €")

    # Suche nach Marke VW
    print("\n--- Suche nach Fahrzeugen der Marke 'VW' ---")
    vw_fahrzeuge = verwaltung.suche_fahrzeuge_nach_marke("vw")
    for f in vw_fahrzeuge:
        verwaltung.zeige_fahrzeugdetails(f)

if __name__ == "__main__":
    main()
