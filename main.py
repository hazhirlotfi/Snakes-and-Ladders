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
        #ladders bottom
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
    print("---" * 13)


def snakeNladders(player):
    snakes = {
        38:17, 
        28:26,
        16:12
    }
    if player in snakes.keys():
        player -= snakes[player]
        print("\tYou got eaten by a SNAKE!")

    ladders = {
        3:11,
        13:13,
        19:13
    }
    if player in ladders.keys():
        print("\tYou climbed a ladder!")
        player += ladders[player]

    return player

print("""
┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐                       
│││├┤ │  │  │ ││││├┤    │ │ │                       
└┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘                       
╔═╗┌┐┌┌─┐┬┌─┌─┐┌─┐  ┌─┐┌┐┌┌┬┐  ╦  ┌─┐┌┬┐┌┬┐┌─┐┬─┐┌─┐
╚═╗│││├─┤├┴┐├┤ └─┐  ├─┤│││ ││  ║  ├─┤ ││ ││├┤ ├┬┘└─┐
╚═╝┘└┘┴ ┴┴ ┴└─┘└─┘  ┴ ┴┘└┘─┴┘  ╩═╝┴ ┴─┴┘─┴┘└─┘┴└─└─┘
""")

input("    Press enter to start the Game:")
print("\n")
print("\tHere is the Board: ")

snl_map(player="")

while True:

    player1_roll = dice()
    input("\tPlayer 1, Press enter: ")
    print("\n")
    print(" " * 13, "Result: ")
    print(f'\tPlayer 1 rolled a {player1_roll}')

    if player1 < 42:
        player1 += player1_roll
        if player1 > 42:
            print('\tMore than 42.\n')
            player1 -= player1_roll
    
    player1 = snakeNladders(player1)
    print(f'\tPlayer 1\'s place is {player1}\n\
    Here is your place on the board: \n')

    snl_map(player1)

    if player1 == 42:
        print(" " * 13,'Player 1 Won!')
        break

    player2_roll = dice()
    input("\tPlayer 2, Press enter: ")
    print("\n")
    print(" " * 13, "Result: ")
    print(f'\tPlayer 2 rolled a {player2_roll}')

    if player2 < 42:
        player2 += player2_roll
        if player2 > 42:
            print('\tMore than 42.\n')
            player2 -= player2_roll

    player2 = snakeNladders(player2)
    print(f'\tPlayer 2\'s place is {player2}\n\
    Here is your place on the board: \n')

    snl_map(player2)

    if player2 == 42:
        print(" " * 13,'Player 2 Won!')
        break