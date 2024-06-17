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

while player1 <= 42 or player2 <= 42:
    input("p1, press enter: ")
    print(f"player1's place is {player1}")
    player1 += dice()
    input('p2 press enter: ')
    print(f"player2's place is {player2}")
    player2 += dice()

if player1 == 42:
    print('player on3 won')

elif player2 == 42:
    print('player two won')

