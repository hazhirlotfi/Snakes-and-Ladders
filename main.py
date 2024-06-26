import random as rnd

naghshe = []

player1 = 1
player2 = 1

def dice():
    return rnd.randint(1,6)

def snl_map(player):
    naghshe.clear()
    for cells in range(1,44):
        #player's place
        if cells == player1:
            naghshe.append('[p1]')            
        elif cells == player2:
            naghshe.append('[p2]')
        #snakes head
        elif cells in (16,28,38):
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

    for i in range(41,-1,-1):
        if (i + 1) % 7 == 0:
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

    ladders = {
        3:11,
        13:13,
        19:13
    }
    if player in ladders.keys():
        print("You climbed a ladder! YAY.")
        player += ladders[player]

    return player

snl_map(player="")

while True:

    player1_roll = dice()
    input("p1, press enter: ")
    print(f'player1 rolled a {player1_roll}')

    if player1 < 42:
        player1 += player1_roll
        if player1 > 42:
            print('more than 42 :(\n')
            player1 -= player1_roll
    
    player1 = snakeNladders(player1)
    print(f'player1\'s place is {player1}\n')

    snl_map(player1)

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

    player2 = snakeNladders(player2)
    print(f'player2\'s place is {player2}\n')

    snl_map(player2)

    if player2 == 42:
        print('player2 won')
        break