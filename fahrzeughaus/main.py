from pkw import PKW
from motorrad import Motorrad
from lkw import LKW
from verwaltung import FahrzeughausVerwaltung

verwaltung = FahrzeughausVerwaltung()
pkw_vw = PKW("VW", "Golf", 2020, 4, 20000, kofferraumvolumen=380)
pkw_bmw= PKW("BMW", "3er", 2021, 4, 25000, kofferraumvolumen=450)
motorrad_yamaha = Motorrad("Yamaha", "MT-07", 2022, 2, 8000)
lkw_man = LKW("MAN", "TGX", 2019, 6, 60000, ladegewicht=10000)

motorrad_yamaha.sitzbank_oeffnen()
motorrad_yamaha.sitzbank_schliessen()
lkw_man.ladung_aufnehmen(500)

verwaltung.fahrzeug_hinzufuegen(pkw_vw)
verwaltung.fahrzeug_hinzufuegen(pkw_bmw)
verwaltung.fahrzeug_hinzufuegen(motorrad_yamaha)
verwaltung.fahrzeug_hinzufuegen(lkw_man)

verwaltung.zeige_alle_fahrzeuge()

print("\n--- Polymorphismus-Demo ---")
for f in verwaltung.fahrzeuge:
    f.starten()
    f.wechsle_reifen()