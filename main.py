"""
Datei: main.py
Autor:Innen: Leo Mayer, Danny Haupt, Tim Weishaupt, Amelie Hager
Datum: 19.03.2026
Kurzbeschreibung:
Dieses Programm ist eine vereinfachte Version des Glückspiels Roulette. 
Der Nutzer kann sein Guthaben aufladen und das Ganze oder nur ein Teil auf entweder eine Farbe, 
eine Zahl oder ein Zahlendrittel setzen.

"""

from gamelogic import altersabfrage, wheel_spin, define_color, check_color, check_number, check_drittel, VALID_FARBEN, VALID_DRITTEL

# Farbcodes für farbige Ausgabe
ROT = "\033[31m"
GRUEN = "\033[32m"
SCHWARZ_TEXT = "\033[90m" # Farbe ist grau wegen Lesbarkeit
RESET = "\033[0m"

VALID_OPTIONEN = ["1", "2", "3", "4"]

def farbtext(text, farbe):
    if farbe == "rot":
        return f"{ROT}{text}{RESET}"
    elif farbe == "grün":
        return f"{GRUEN}{text}{RESET}"
    elif farbe == "schwarz":
        return f"{SCHWARZ_TEXT}{text}{RESET}"
    else:
        return text

# Spiel starten
def spiel_starten():
    print(
        "\n=============================================\n"
        "⚠️ ACHTUNG – Glücksspiel kann süchtig machen!\n"
        "=============================================\n\n"

        "Glücksspiel kann zur Abhängigkeit führen.\n"
        "Bitte spielen Sie verantwortungsvoll.\n\n"

        "Beratung & Unterstützung:\n"
        "📞 0800 1 37 27 00 (kostenlos & anonym)\n\n"

        "=============================================\n")
    
    if not altersabfrage():
        return
    
    print(
            "=============================================\n"
            "🎰      WILLKOMMEN ZUM ROULETTE-SPIEL      🎰\n"
            "=============================================\n")
    
    # Guthaben aufladen & Einsatz bestimmen
    while True:
        print("Wie viele Jetons möchten Sie aufladen?")
        guthaben = input("Aufladen: ").strip()

        try: 
            guthaben = int(guthaben)
            if guthaben > 0:
                break
            else: 
                print("Bitte geben Sie eine Zahl größer als 0 ein.")
        except ValueError:
             print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
            
    while guthaben > 0:
            print(f"Ihr Guthaben beträgt: {guthaben} Jetons.")
            print("Wie viele Jetons möchten Sie diese Runde setzen?")

            while True:
                rundeinsatz = input("Einsatz: ").strip()

                try:
                    rundeinsatz = int(rundeinsatz)

                    if rundeinsatz <= 0:
                        print("Der Einsatz muss mindestens 1 Jeton betragen.")
                    elif rundeinsatz > guthaben:
                        print("Sie können nicht mehr Jetons setzen, als Ihr Guthaben beträgt.")
                    else:
                        if rundeinsatz == guthaben:
                            print("Sie setzen ihr gesamtes Guthaben, Viel Glück!")
                        break
                    
                except ValueError:
                     print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")
        
            # Menüoptionen
            print(f"\nAuf was möchten Sie Ihren Einsatz von {rundeinsatz} Jetons setzen?")
            print("Wählen Sie eine der folgenden Optionen:")
            print("1 = Auf eine Farbe setzen")
            print("2 = Auf eine Zahl setzen")
            print("3 = Auf ein Drittel der Zahlen setzen")
            print("4 = Spiel beenden")

            spielauswahl = input("Bitte wählen Sie ihre Option: ").strip()

            # Farbwette
            if spielauswahl == "1":
                print("Sie können auf folgende Farben setzen:")
                print(
                    farbtext("Rot", "rot"),
                    farbtext("Grün", "grün"),
                    farbtext("Schwarz", "schwarz")
                )
                 
                while True:
                    farbe = input("Welche Farbe wählen Sie?: ").lower().strip()

                    if farbe in VALID_FARBEN:
                        break
                    else:
                        print("Ungültige Eingabe. Bitte geben Sie 'rot', 'schwarz' oder 'grün' ein.")

                result = wheel_spin()
                ergebnis_farbe = define_color(result)

                print(f"Ergebnis: {result} ({farbtext(ergebnis_farbe, ergebnis_farbe)})")

                if check_color(farbe, result):
                    print("Sie haben gewonnen!")
                    guthaben = guthaben + rundeinsatz
                else:
                    print("Sie haben verloren!")
                    guthaben = guthaben - rundeinsatz
            
            # Zahlenwette
            elif spielauswahl == "2":
                while True:
                    nummer = input("Auf welche Zahl möchten Sie wetten? (0 - 36): ").strip()

                    try:
                        nummer = int(nummer)
                        if 0 <= nummer <= 36:
                            break
                        else:
                            print("Ungültige Eingabe. Bitte geben Sie eine Zahl von 0 bis 36 ein.")
                    except ValueError:
                     print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

                result = wheel_spin()
                ergebnis_farbe = define_color(result)

                print("Sie haben auf", nummer, "gewettet")
                print(f"Ergebnis: {result} ({farbtext(ergebnis_farbe, ergebnis_farbe)})")

                if check_number(nummer, result):
                    print("Sie haben gewonnen!")
                    guthaben = guthaben + (rundeinsatz * 36)
                else:
                    print("Sie haben verloren!")
                    guthaben = guthaben - rundeinsatz 


            # Auf Range der Zahlen setzen
            elif spielauswahl == "3":
                print("Sie können auf folgende Drittel setzen: ")
                print("1 = 1 bis 12")
                print("2 = 13 bis 24")
                print("3 = 25 bis 36")

                while True:
                    drittel = input("Auf welches Drittel möchten Sie setzen? (1, 2 oder 3): ").strip()

                    if drittel in VALID_DRITTEL:
                        break
                    else:
                        print("Ungültige Eingabe. Bitte wählen sie 1, 2 oder 3.")

                result = wheel_spin()
                ergebnis_farbe = define_color(result)

                print("Sie haben auf Drittel", drittel, "gewettet") 
                print(f"Ergebnis: {result} ({farbtext(ergebnis_farbe, ergebnis_farbe)})")

                if check_drittel(drittel, result):
                    print("Sie haben gewonnen!")
                    guthaben = guthaben + (rundeinsatz * 3)
                else:
                    print("Sie haben verloren!")
                    guthaben = guthaben - rundeinsatz


            # Spiel beenden
            elif spielauswahl == "4":
                print("Game over...")
                return

            else:
                print("Ungültige Eingabe. Bitte wählen Sie eine der Optionen 1, 2, 3 oder 4.")

    # Auswahl bei leerem Guthaben
    print("\nSie haben kein Guthaben mehr übrig.")

    while True:
        neustart = input("Möchten Sie neu starten? (ja/nein): ").lower().strip()

        if neustart == "ja":
            spiel_starten()
            return
        elif neustart == "nein":
            print("Programm beendet.")
            return
        else:
            print("Ungültige Eingabe. Bitte geben Sie ja oder nein ein.")

# Startbedingung
while True:
    starteingabe = input("Geben Sie 'start' ein, um das Spiel zu beginnen: ").lower().strip()

    if starteingabe == "start":
        spiel_starten()
        break  
    else: 
        print("Sie müssen 'Start' eingeben, um das Spiel zu beginnen.")
