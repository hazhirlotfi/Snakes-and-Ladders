import random as rnd

naghshe = []

player = 1

def dice():
    return rnd.randint(1,6)

def snl_map(player):
    naghshe.clear()
    for row in range(6, 0, -1):
        row_cells = []
        for col in range(1, 8):
            cell_num = (row - 1) * 7 + col
            if cell_num <= 42:
                if cell_num == player:
                    row_cells.append('[p1]')
                elif cell_num in (16, 28, 38):
                    row_cells.append('[$]')
                elif cell_num in (2, 4, 21):
                    row_cells.append('[?]')
                elif cell_num in (3, 13, 19):
                    row_cells.append('[#]')
                elif cell_num in (14, 26, 32):
                    row_cells.append('[%]')
                else:
                    row_cells.append('[-]')
            else:
                row_cells.append('   ')
        if row % 2 == 0:
            row_cells.reverse()
        naghshe.extend(row_cells)

    for i in range(len(naghshe)):
        if (i + 1) % 7 == 0:
            print(naghshe[i])
            print()
        else:
            print(naghshe[i], end="    ")
    print()
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
print()
print("\tHere is the Board:\n ")

snl_map(player)

while True:

    player_roll = dice()
    input("\tPlayer, Press enter: ")
    print()
    print(" " * 13, "Result: ")
    if player == 42:
        print(" " * 13,"You Won!")    
        break
    print(f'\tPlayer rolled a {player_roll}')

    if player < 42:
        player += player_roll
        if player > 42:
            print('\tMore than 42.\n')
            player -= player_roll

    player = snakeNladders(player)
    print(f'\tPlayer\'s place is {player}\n\
    Here is your place on the board: \n')

    snl_map(player)
