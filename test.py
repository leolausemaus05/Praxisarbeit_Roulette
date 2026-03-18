"""import os

def bildschirm_freigeben():
    os.system("cls" if os.name == "nt" else "clear")
"""


def altersabfrage():
    while True:
        altersabfrage_antwort = input("Sind Sie mindestens 18 Jahre alt? (ja/nein) ").lower().strip()
        if altersabfrage_antwort == "ja":
            print("\nWillkommen zum Roulette-Spiel!\n")
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

                "Zu Ihrem eigenen Schutz wird das Spiel hiermit beendet."

                "=============================================\n")
            
            return False
        else:
            print("\nUngültige Eingabe. Bitte geben Sie 'ja' oder 'nein' ein.\n")


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
    print("Altersabfrage erfolgreich. Das Spiel kann gestartet werden.")
else:
    print("Altersabfrage fehlgeschlagen. Das Spiel wird beendet.")