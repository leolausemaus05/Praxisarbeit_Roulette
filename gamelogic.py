# Datei: gamelogic.py
# Enthält die Spiellogik des Spiels Roulette

import random

farben = ["red", "black", "green"]
zahlen = list[range(0, 37)]

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