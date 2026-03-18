"""
Projektname: Roulette-Spiel
Autoren: Leo Mayer, Danny Haupt, Tim Weißhaupt, Amelie Hager
Datum:

Beschreibung: Vereinfachte Version des Glückspiels Roulette

"""

from gamelogic import altersabfrage, wheel_spin, define_color, check_color, check_number, farben, zahlen, check_drittel

farbe_1 = "Rot"
farbe_2 = "Schwarz"
farbe_3 = "Grün"

# Spiel starten
start = "start"

starteingabe = input("Geben Sie 'Start' ein, um das Spiel zu beginnen: ").lower().strip()

if starteingabe == start:

    print(
        "\n=============================================\n"
        "⚠️ ACHTUNG – Glücksspiel kann süchtig machen!\n"
        "=============================================\n\n"

        "Glücksspiel kann zur Abhängigkeit führen.\n"
        "Bitte spielen Sie verantwortungsvoll.\n\n"

        "Beratung & Unterstützung:\n"
        "📞 0800 1 37 27 00 (kostenlos & anonym)\n\n"

        "=============================================\n")
    
    if altersabfrage():
        print(
            "=============================================\n"
            "🎰      WILLKOMMEN ZUM ROULETTE-SPIEL      🎰\n"
            "=============================================\n")
    else:
        exit()



    while True:
        print("Wie viele Jetons möchten Sie aufladen? ")
        guthaben = input("Aufladen: ")
        try:
            guthaben = int(guthaben)
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            continue
       
        if guthaben <= 0:
            print("Der Betrag muss mindestens 1 Jeton betragen.")
            continue

        break

    # Spielschleife, läuft solange Guthaben vorhanden ist
    while guthaben > 0:
    # Menüauswahl
        print("Ihr Guthaben beträgt: ", guthaben , " Jetons")
        print("Wie viel Jetons möchten Sie diese Runde setzen? ")
        while True:
            rundeneinsatz = input("Einsatz: ")

            try:
                rundeneinsatz = int(rundeneinsatz)
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
                continue

            if rundeneinsatz > guthaben:
                print("Sie können nicht mehr Jetons setzen, als ihr Guthaben beträgt.")
                continue
            elif rundeneinsatz <= 0:
                print("Der Einsatz muss mindestens 1 Jeton betragen.")
                continue
            elif rundeneinsatz == guthaben:
                print("Sie setzen ihr gesamtes Guthaben, Viel Glück!")
                
            break

        print("Auf was möchten Sie Ihren Einsatz von ", rundeneinsatz, " Jetons setzen? ")
        print("Wählen Sie eine der folgenden Optionen:")
        print("1 = Auf eine Farbe setzen")
        print("2 = Auf eine Zahl setzen")
        print("3 = Auf ein Drittel der Zahlen setzen")
        print("4 = Spiel beenden")

        spielauswahl = input("Bitte wählen Sie ihre Option: ")

        # Farbwette
        if spielauswahl == "1":
            print("Sie können auf folgende Farben setzen:")
            print(farbe_1, farbe_2, farbe_3)

            farbe = input("Auf welche Farbe möchten Sie wetten? (Rot, Schwarz, Grün) ").lower().strip()
            
            result = wheel_spin()
            print("Sie haben auf", farbe, "gewettet")
            print("Ergebnis:", result, define_color(result))

            if check_color(farbe, result):
                print("Sie haben gewonnen!")
                guthaben = guthaben + (rundeneinsatz * 2)
            else:
                print("Sie haben verloren!")
                guthaben = guthaben - rundeneinsatz

        # Zahlenwette
        elif spielauswahl == "2":
            print ("Sie können auf folgende Zahlen setzen: 0 - 36")

            nummer = int(input("Auf welche Zahl möchten Sie wetten? "))

            result = wheel_spin()
            print("Sie haben auf", nummer, "gewettet")
            print("Ergebnis:", result, define_color(result))

            if check_number(nummer, result):
                print("Sie haben gewonnen!")
                guthaben = guthaben + (rundeneinsatz * 36)
            else:
                print("Sie haben verloren!")
                guthaben = guthaben - rundeneinsatz

        # Auf Range der Zahlen setzen
        elif spielauswahl == "3":
            print("Sie können auf folgende Drittel setzen: 1 - 12, 13 - 24, 25 - 36")

            drittel = input("Auf welches Drittel möchten Sie setzen? (1, 2 oder 3) ")
            result = wheel_spin()
            print("Sie haben auf Drittel", drittel, "gewettet") 
            print("Ergebnis:", result, define_color(result))    

            if check_drittel(drittel, result):
                print("Sie haben auf das richtige Drittel gesetzt, Sie haben gewonnen!")
                guthaben = guthaben + (rundeneinsatz * 3)
            else:
                print("Sie haben verloren!")
                guthaben = guthaben - rundeneinsatz

        # Spiel beenden
        elif spielauswahl == "4":
            print("Game over")
            break

        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine der Optionen 1, 2, 3 oder 4.")

    # Guthaben leer
    if guthaben <= 0:
        print("Sie haben kein Guthaben mehr übrig. Das Spiel ist hiermit beendet. Viel Glück beim nächsten Mal!")
        
else: 
    print("Sie müssen 'Start' eingeben, um das Spiel zu beginnen")
