"""
Projektname: Roulette-Spiel
Autoren: Leo Mayer, Danny Haupt, Tim Weishaupt, Amelie Hager
Datum:

Beschreibung: Vereinfachte Version des Glückspiels Roulette

"""

from gamelogic import wheel_spin, define_color, check_color, check_number, farben, zahlen

possibility_1 = "\033[91mred\033[0m"
possibility_2 = "\033[90mblack\033[0m"
possibility_3 = "\033[92mgreen\033[0m"

# Spiel starten
start = "Go"
print("Type in " + start + " to start the Roulette Game:")

check = input()

if check == start:

    credit = int(input("How many euros do you want to bet? "))

    # Spielschleife, läuft solange Guthaben vorhanden ist
    while credit > 0:
    # Menüauswahl
        print("Game on...")
        print("Your credit is:", credit)
        print("1 = Bet on color")
        print("2 = Bet on number")
        print("4 = End game")
        print("3 = Bet on range of numbers")

        choice = input("Your choice: ")

        # Farbwette
        if choice == "1":
            print("Available colors:")
            print(possibility_1, possibility_2, possibility_3)

            color = input("On what color do you want to bet? ").lower()
            
            result = wheel_spin()
            print("You bet on", color)
            print("Result:", result, define_color(result))

            if check_color(color, result):
                print("You won!")
                credit = credit + credit
            else:
                print("you lost!")
                credit = credit - credit

        # Zahlenwette
        elif choice == "2":
            print ("Available numbers: 0 - 36")

            number = int(input("On what number do you want to bet? "))

            result = wheel_spin()
            print("You bet on", number)
            print("Result:", result, define_color(result))

            if check_number(number, result):
                print("You won!")
                credit = credit + credit
            else:
                print("You lost!")
                credit = credit - credit

        # Auf Range der Zahlen setzen
        elif choice == "3":
            print("Available ranges: 1 - 12, 13 - 24, 25 - 36")


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
    print("You have to type in 'Go' to start the game")
