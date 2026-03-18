"""
Projektname: Roulette-Spiel
Autoren: Leo Mayer, Danny Haupt, Tim Weißhaupt, Amelie Hager
Datum:

Beschreibung: Vereinfachte Version des Glückspiels Roulette

"""

from gamelogic import altersabfrage, wheel_spin, define_color, check_color, check_number, farben, zahlen, check_drittel

possibility_1 = "red"
possibility_2 = "black"
possibility_3 = "green"

# Spiel starten
start = "start"

check = input("Geben Sie 'Start' ein, um das Spiel zu beginnen: ").lower().strip()

if check == start:

    print(
        "=============================================\n"
        "⚠️ ACHTUNG – Glücksspiel kann süchtig machen!\n"
        "=============================================\n\n"

        "Glücksspiel kann zur Abhängigkeit führen.\n"
        "Bitte spielen Sie verantwortungsvoll.\n\n"

        "Hilfe:\n"
        "📞 0800 1 37 27 00 (kostenlos & anonym)\n"

        "=============================================\n")
    
    if altersabfrage():
        print("Willkommen zum Roulette-Spiel!\n")
    else:
        exit()

    credit = int(input("Wie viele Coins möchten Sie setzen? "))

    # Spielschleife, läuft solange Guthaben vorhanden ist
    while credit > 0:
    # Menüauswahl
        print("Spiel gestartet...")
        print("Ihr Guthaben beträgt:", credit , "Coins")
        print("1 = Auf eine Farbe setzen")
        print("2 = Auf eine Zahl setzen")
        print("3 = Auf ein Drittel der Zahlen setzen")
        print("4 = Spiel beenden")

        choice = input("Bitte wählen Sie ihre Option: ")

        # Farbwette
        if choice == "1":
            print("Sie können auf folgende Farben setzen:")
            print(possibility_1, possibility_2, possibility_3)

            color = input("Auf welche Farbe möchten Sie wetten? (red, black, green) ").lower()
            
            result = wheel_spin()
            print("Sie haben auf", color, "gewettet")
            print("Ergebnis:", result, define_color(result))

            if check_color(color, result):
                print("Sie haben gewonnen!")
                credit = credit * 2
            else:
                print("Sie haben verloren!")
                credit = credit - credit

        # Zahlenwette
        elif choice == "2":
            print ("Sie können auf folgende Zahlen setzen: 0 - 36")

            number = int(input("Auf welche Zahl möchten Sie wetten? "))

            result = wheel_spin()
            print("Sie haben auf", number, "gewettet")
            print("Ergebnis:", result, define_color(result))

            if check_number(number, result):
                print("Sie haben gewonnen!")
                credit = credit * 36
            else:
                print("Sie haben verloren!")
                credit = credit - credit

        # Auf Range der Zahlen setzen
        elif choice == "3":
            print("Sie können auf folgende Drittel setzen: 1 - 12, 13 - 24, 25 - 36")

            drittel = input("Auf welches Drittel möchten Sie setzen? (1, 2 oder 3) ")
            result = wheel_spin()
            print("Sie haben auf Drittel", drittel, "gewettet") 
            print("Ergebnis:", result, define_color(result))    

            if check_drittel(drittel, result):
                print("Sie haben auf das richtige Drittel gesetzt, Sie haben gewonnen!")
                credit = credit * 3
            else:
                print("Sie haben verloren!")
                credit = credit - credit

        # Spiel beenden
        elif choice == "4":
            print("Game over")
            break

        else:
            print("You have to choose option 1, 2 or 3")

    # Guthaben leer
    if credit <= 0:
        print("You have no credit left")
        
else: 
    print("You have to type in 'Start' to start the game")
