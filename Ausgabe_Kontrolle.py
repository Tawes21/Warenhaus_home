from Variablen import *

def ausgabe_controlle(user_choice):
    if 1 <= user_choice <= len(schrauben_liste):
        pack_name, pack_preis = schrauben_liste[user_choice -1]
        gesamt_kosten = schrauben_liste[user_choice -1][1] + versand
        print(f"Du hast dich für das {pack_name}entschieden! {pack_preis:.2f} €")
        print(f"Die gesamtkosten für deine Bestellung betragen {gesamt_kosten:.2f}€")
        if gesamt_kosten <= 70.00: 
            print("Sie erhalten einen Geschenkgutschein von 15 € auf Ihre nächste Bestellung")
    else: 
        print("wählen sie ein Produkt aus.")


