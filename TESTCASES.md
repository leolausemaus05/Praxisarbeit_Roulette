# Testcases

Abfrage 1: Geben sie 'start' ein, um das Spiel zu beginnen:

Eingabe 1: start

Erwartete Ausgabe: Abfrage 2
Eingtroffene Ausgabe: Abfrage 2

Abfrage 2: Sind Sie mindestens 18 Jahre alt?

Eingabe 2: ja

Erwartete Ausgabe: Abfrage 3
Eingetroffen Aussage: Abfrage 3

Abfrage 3: Wie viele Jetons möchten Sie aufladen?

Eingabe 3: 100

Erwartete Ausgabe: Ihr Guthaben beträgt 100 Jetons. & Abfrage 4
Eingetroffene Ausgabe: Ihr Guthaben beträgt 100 Jetons. & Abfrage 4

Abfrage 4: Wie viele Jetons möchten Sie diese Runde setzen.

Eingabe 4: 100

Erwartete Ausgabe: Abfrage 5
Eingetroffene Ausgabe: Abfrage 5

Abfrage 5: Wählen Sie eine der vier Setzoptionen (1-4).

# Option 1

Einagbe 5.1: 1 (Auf eine Farbe setzen)

Erwartete Ausgabe: Abgrage 6.1
Eingetroffene Ausgabe: Abfrage 6.1

Abfrage 6.1: Welche Frabe wählen Sie? (Rot, Grün, Schwarz)

Eigabe 6.1: Rot

Erwartete Ausgabe: Random Farbe 
                    bei Eingabe 6 = Random Farbe gewonnen -> Guthaben 200 Jetons -> Abfrage 5
                    sonst verloren -> Guthaben 0 Jetons -> kein Guthaben mehr -> Abfrage 7

Eingetroffene Ausgabe: Rot (7) Sie haben gewonnen! Ihr Guthabe beträgt 200 Jetons.
                        -> Abfrage 5

# Option 2

Einagbe 5.2: 2 (Auf eine Zahl setzen)

Erwartete Ausgabe: Abgrage 6.2
Eingetroffene Ausgabe: Abfrage 6.2

Abfrage 6.2: Welche Zahl wählen Sie? (0-36)

Eigabe 6.2: Zahl zwischen 0 und 36 (ich wähle 15)

Erwartete Ausgabe: Random Farbe 
                    bei Eingabe 6.2 = Random Zahl gewonnen -> Guthaben 3600 Jetons -> Abfrage 5
                    -> verloren -> Guthaben 0 Jetons -> kein Guthaben mehr 
                    -> Abfrage 7

Eingetroffene Ausgabe: 8 (Schwarz) Sie haben verloren! Ihr Guthabe beträgt 0 Jetons. 
                        -> kein Guthaben mehr 
                        -> Abfrage 7

Abfrage 7: Möchten Sie Neustarten?

Eingabe: ja/nein

Erwartete Ausgabe: ja-> Abfrage 1
                   nein -> Programm beendet
Eigetroffen Ausgabe: ja-> Abfrage 1
                     nein -> Programm beendet

# Option 3

Einagbe 5.3: 3 (Auf ein Drittel setzen)

Erwartete Ausgabe: Abgrage 6.3
Eingetroffene Ausgabe: Abfrage 6.3

Abfrage 6.3: Welches Drittel wählen Sie? (1 = 1-12, 2 = 13-25, 3 = 26-36)

Eigabe 6.3: 2

Erwartete Ausgabe: Random Drittel
                    bei Eingabe 6.3 = Random Drittel gewonnen -> Guthaben 300 Jetons -> Abfrage 5
                    -> verloren -> Guthaben 0 Jetons -> kein Guthaben mehr 
                    -> Abfrage 7

Eingetroffene Ausgabe: 2 (Schwarz) Sie haben verloren! Ihr Guthabe beträgt 0 Jetons. 
                        -> kein Guthaben mehr 
                        -> Abfrage 7

Abfrage 7: Möchten Sie Neustarten?

Eingabe: ja/nein

Erwartete Ausgabe: ja-> Abfrage 1
                   nein -> Programm beendet
Eigetroffen Ausgabe: ja-> Abfrage 1
                     nein -> Programm beendet

# Option 4:

Einagbe 5.4: 4 (Spiel beenden)

Erwartete Ausgabe: Game over...
Eingetroffene Ausgabe: Game over...