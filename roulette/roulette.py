possibillity_1= "red"
possibillity_2= "black"
possibillity_3= "green"

Zahlen = (0-36)

Eingabe_1= "Go"

print("Type in " + Eingabe_1 + " to start the Roulette Game")

if input() == Eingabe_1:
    print("How much euros do you want to bet?")
    bet = int(input(""))
    print("You bet " + str(bet) + " euros!")

else:
    print("You have to type in " + Eingabe_1 + " to start the game")

print("On what color or number do you want to bet on? \033[31m red\033[0m or \033[30m black\033[0m or \033[32m green\033[0m?")

if input() == possibillity_1:
    print("You bet on \033[31m red\033[0m!")

elif input() == possibillity_2:
    print("You bet on \033[30m black\033[0m!")

elif input() == possibillity_3:
    print("You bet on \033[32m green\033[0m!")

elif input() in Zahlen:
    print("You bet on the number " + str(input()) + "!")

else:
    print("Invalid color or number choice!")

