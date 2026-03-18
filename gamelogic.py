# Datei: gamelogic.py
# Enthält die Spiellogik des Spiels Roulette

import random

farben = ["red", "black", "green"]
zahlen = list[range(0, 36)]

# Altersabfrage, um sicherzustellen, dass der Spieler alt genug ist, um zu spielen
def altersabfrage():
    while True:
        altersabfrage_antwort = input("Sind Sie mindestens 18 Jahre alt? (ja/nein) ").lower().strip()
        if altersabfrage_antwort == "ja":
            print("\nAltersabfrage erfolgreich.\n")
            return True
        elif altersabfrage_antwort == "nein":
            print(
                "\nSie sind zu jung, um dieses Spiel zu spielen.\n\n"

                "In Deutschland ist die Teilnahme am Glücksspiel\n"
                "gemäß dem Jugendmedienschutz-Staatsvertrag (JMStV)\n"
                "und dem Glücksspielstaatsvertrag (GlüStV) auf\n"
                "volljährige Personen beschränkt. Dies dient dem \n"
                "Schutz von Minderjährigen vor Suchtgefahren sowie \n"
                "finanziellen und sozialen Risiken.\n\n"

                "Zu Ihrem eigenen Schutz wird das Spiel hiermit beendet.\n\n"

                "=============================================\n")
            
            return False
        else:
            print("\nUngültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein.\n")

# Rad wird gedreht, eine zufällige Zahl zwischen 0 und 36 ist das Ergebnis
def wheel_spin():
    result = random.randint(0, 36)
    return result

# Zahl wird analysiert um Farbe des Feldes herauszufinden
def define_color(result):
    if result == 0:
        return "green"
    elif result % 2 == 0:
        return "black"
    else:
        return "red"
    
# Farbgewinn überprüfen
def check_color(color, result):
    return color == define_color(result)

# Zahlengewinn überprüfen
def check_number(number, result):
    return number == result

# Überprüfen, ob die Zahl im richtigen Drittel liegt
def check_drittel(drittel, result):
    if drittel == "1":
        return result >= 1 and result <= 12
    elif drittel == "2":
        return result >= 13 and result <= 24
    elif drittel == "3":
        return result >= 25 and result <= 36