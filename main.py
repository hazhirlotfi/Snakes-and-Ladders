import random as rnd

naghshe = []

player = 1

def dice():
    return rnd.randint(1,6)

def snl_map(player):
    naghshe.clear()
    for cells in range(1,44):
        #player's place
        if cells == player:
            naghshe.append('[D]')
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

snl_map(player)

while True:

    player_roll = dice()
    input("\tPlayer, Press enter: ")
    print("\n")
    print(" " * 13, "Result: ")
    print(f'\tPlayer rolled a {player_roll}')

    if player < 42:
        player += player_roll
        if player > 42:
            print('\tMore than 42.\n')
            player -= player_roll
    else:
        print(" " * 13,"You Won!")    
        break
    
    player = snakeNladders(player)
    print(f'\tPlayer\'s place is {player}\n\
    Here is your place on the board: \n')

    snl_map(player)
