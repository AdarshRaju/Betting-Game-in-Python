print('Betting Game')

import random

Money = 1000;
Rounds = int(input("Enter no. of rounds:"))

Marbles ="GGGGGBRRRW"


Bet_final = 0;
for i in range(Rounds):
    
    Bet_amount = int(input("Enter your bet:"))
    Selected = random.choice(Marbles)

    if Selected == "G":
        Bet_final = Bet_amount
    elif Selected == "R":
        Bet_final = -Bet_amount
    elif Selected == "B":
        Bet_final = 10*Bet_amount
    elif Selected == "W":
        Bet_final = -5*Bet_amount

    Money = Money + Bet_final
    print(Money)
    
    if Money <= 500:
        print("Game Over")
        break
