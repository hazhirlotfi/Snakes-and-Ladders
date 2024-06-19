import random as rnd

naghshe = []

def dice():
    return rnd.randint(1,6)

for cells in range(42):
    #snakes head
    if cells in (16,28,38):
        naghshe.append('[$]')
    #snakes tail
    elif cells in (2,4,21):
        naghshe.append('[?]')
    #ladders botton
    elif cells in (3, 13, 19):
        naghshe.append('[#]')    
    #ladders top
    elif cells in (14, 26, 32):
        naghshe.append('[%]')
    else:
        naghshe.append('[-]')

for i in range(42):
    if i % 6 == 0:
        print('\n')
    print(naghshe[i], end = "   ")
print("\n")


def snakeNladders(player):
    snakes = {
        38:17, 
        28:26,
        16:12
    }
    if player in snakes.keys():
        player -= snakes[player]
        print("You got eaten by a SNAKE!")
        print(f"Your place is {player}")

    ladders = {
        3:11,
        13:13,
        19:13
    }
    if player in ladders.keys():
        player += ladders[player]
        print("You climbed a ladder! YAY.")
        print(f"Your place is {player}")

player1 = 0
player2 = 0

#game logic: 
while True:

    player1_roll = dice()
    input("p1, press enter: ")
    print(f'player1 rolled a {player1_roll}')

    if player1 < 42:
        player1 += player1_roll
        if player1 > 42:
            print('more than 42 :(\n')
            player1 -= player1_roll
    
    if snakeNladders():
        continue

    print(f'player1\'s place is {player1}\n')

    if player1 == 42:
        print('player1 won')
        break

    player2_roll = dice()
    input("p2, press enter: ")
    print(f'player2 rolled a {player2_roll}')

    if player2 < 42:
        player2 += player2_roll
        if player2 > 42:
            print('more than 42 :(\n')
            player2 -= player2_roll

    if snakeNladders():
        continue

    print(f'player2\'s place is {player2}\n')

    if player2 == 42:
        print('player2 won')
        break