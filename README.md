# Praxisarbeit_Roulette

Diese Programm ist eine vereinfachte Version des Glückspiels Roulette.
Als Nutzer kann man Guthaben aufladen und entweder auf 
- Farben (rot, grün, schwarz)
- einzelne Zahlen ( von 0 bis 36)
- Zahlendrittel (1-12, 13-24, 25-36)
setzen.

Das Spiel läuft bis kein Guthaben mehr vorhanden ist oder das Spiel vom Nutzer beendet wird.

Um den Jugendschutz zu gewähren gibt es anfangs eine Altersabfrage, das Spiel ist ab 18 Jahren erlaubt.

---

Python Version: 3.14.3
Keine zusätzlichen Bibliotheken notwenig, nur 'random'

---

Um das Programm zu starten folgt man diesem Ablauf:

1. Datei 'main.py' ausführen
2. Im Terminal '"start"' eingeben
3. Anweisungen folgen

---

Beispielhafte Nutzung:

Geben Sie 'start' ein, um das Spiel zu beginnen: start

Sind Sie mindestens 18 Jahre alt? (ja/nein) ja

Altersabfrage erfolgreich.

Wie viele Jetons möchten Sie aufladen?
Aufladen: 100
Ihr Guthaben beträgt: 100 Jetons.
Wie viele Jetons möchten Sie diese Runde setzen?
Einsatz: 10

Auf was möchten Sie Ihren Einsatz von 10 Jetons setzen?
Wählen Sie eine der folgenden Optionen:
1 = Auf eine Farbe setzen
2 = Auf eine Zahl setzen
3 = Auf ein Drittel der Zahlen setzen
4 = Spiel beenden
Bitte wählen Sie ihre Option: 2
Auf welche Zahl möchten Sie wetten? (0 - 36): 15
Sie haben auf 15 gewettet
Ergebnis: 30 (schwarz)
Sie haben verloren!

---

Funktionen im Programm:

- 'altersabfrage()'
Prüft ob Nutzer alt genug ist um zu spielen.
- 'wheel_spin()'
Erzeugt eine zufällige Zahl zwischen 0 und 36.
- 'define_color(result)'
Bestimmt Farbe der gezogenen Zahl
- 'check_color(farbe, result)'
Prüft ob die gewählte Farbe Gewinn entspricht.
- 'check_number(nummer, result)'
Prüft ob die gewählte Zahl Gewinn entspricht.
- 'check_drittel(drittel, result)'
Prüft ob Gewinnzahl in gewähltem Drittel liegt.

---

Projektstruktur:

project/
|
|── main.py
|── gamelogic.py
|── README.md
|── TESTCASES.md
|── flowchart.pdf

---

Teammitglieder:

- Leo Mayer
- Danny Haupt
- Tim Weishaupt
- Amelie Hager

---

Verwendete Module:

- 'random'
Wird verwendet um zufällige Zahlen zwischen 0 und 36 zu erzeugen.

---

Hinweis:

Dieses Spiel ist eine vereinfachte Simulation und entspricht nicht exakt den realen Roulette-Regeln.