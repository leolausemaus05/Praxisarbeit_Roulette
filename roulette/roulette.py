possibillity_1= "red"
possibillity_2= "black"
possibillity_3= "green"

Zahlen = (0-36)

Eingabe_1= "Start"

print("Type in " + Eingabe_1 + " to start the Roullete Game")

if input() == Eingabe_1:
    print("How much euros do you want to bet?")
    bet = int(input(""))

else:
    print("You have to type in " + Eingabe_1 + " to start the game")

print("On what color do you want to bet on? Red or Black or Green?")
