# Testcases

Testcase 1:

Abfrage 1: Geben sie 'start' ein, um das Spiel zu beginnen:

Eingabe: start

Erwartete Ausgabe: Abfrage 2
Eingtroffene Ausgabe: Abfrage 2

Abfrage 2: Sind Sie mindestens 18 Jahre alt?

Eingabe: ja

Erwartete Ausgabe: Abfrage 3
Eingetroffen Aussage: Abfrage 3

Abfrage 3: Wie viele Jetons möchten Sie aufladen?

Eingabe 100

Erwartete Ausgabe: Ihr Guthaben beträgt 100 Jetons. & Abfrage 4
Eingetroffene Ausgabe: Ihr Guthaben beträgt 100 Jetons. & Abfrage 4

Abfrage 4: Wie viele Jetons möchten Sie diese Runde setzen.

Eingabe: 50

Erwartete Ausgabe: Abfrage 5
Eingetroffene Ausgabe: Abfrage 5

Abfrage 5: Wählen Sie eine der vier Setzoptionen (1-4).

Einagbe: 1 (Auf eine Farbe setzen)

Erwartete Ausgabe: Abgrage 6.1
Eingetroffene Ausgabe: Abfrage 6.1

Abfrage 6.1: Welche Frabe wählen Sie? (Rot, Grün, Schwarz)

Eigabe: Rot

Erwartete Ausgabe: Random Farbe 
                    bei Rot gewonnen -> Guthaben 150 Jetons
                    sonst verloren -> Guthaben 50 Jetons

                    Sprung auf Abfrage 5

Eingetroffene Ausgabe: Rot (7) Sie haben gewonnen! Ihr Guthabe beträgt 200 Jetons. 
                       Abfrage 5

# Moglicher Fehler bei der Farb-Gewinn-Addition
