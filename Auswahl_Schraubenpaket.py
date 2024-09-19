from Variablen import *

def auswahl_schraubenpacket():
    try:
        auswahl_text = "Bitte wählen Sie aus den Schrauben-Paketen aus: \n"
        for i, (pack_name, pack_price) in enumerate(schrauben_liste, start = 1):
            auswahl_text += f"{i} für {pack_name} für {pack_price} € \n"

        auswahl = int(input(auswahl_text))
        if 1 <= auswahl <= len(schrauben_liste):
            return auswahl
        else:
                print("Bitte wählen sie aus den gültigen optinen.")

    except ValueError:
        print("Die Eingabe wird als Zahl benötigt")
        exit()
