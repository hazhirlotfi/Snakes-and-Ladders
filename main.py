import random as rnd

naghshe = []



def dice():
    return rnd.randint(1,6)

"Map for Snakes and Ladders"
for i in range(1,43):
    if i in (22,38,40):
        naghshe.append('[?]')
    elif i in (24,25,39):
        naghshe.append('[#]')
    elif i in (11,14,26):
        naghshe.append('[%]')
    elif i in (2,16,28):
        naghshe.append('[$]')
    else: 
        naghshe.append('[-]')

for i in range(len(naghshe)):
    if i > 0:
        if i % 6 == 0:
            print('\n')
    print(naghshe[i], end= '   ')
print('\n')
"'till here"

player1 = 0
player2 = 0

while True:
    input("p1, press enter: ")
    print(f'player1 rolled a {dice()}')

    if player1 + dice() <= 42:
        player1 += dice()
    print(f'player1\'s place is {player1}')

    if player1 == 42:
        print('player1 won')
        break


    input("p2, press enter: ")
    print(f'player2 rolled a {dice()}')

    if player2 + dice() <= 42:
        player2 += dice()
    print(f'player2\'s place is {player2}')

    if player2 == 42:
        print('player2 won')
        break