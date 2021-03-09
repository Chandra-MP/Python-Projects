import random
import sys

print('ROCK', 'PAPER', 'SCISSORS')

wins = 0
lossess = 0
ties = 0

while True:
    print('wins :',  wins)
    print('losses :',  lossess)
    print('ties :',  ties)
    while True:
        print('Enter your turn (rock(r),paper(p),scissors(s)):')
        move = input()
        if move=='q':
            quit();
        elif move=='r' or move=='p' or move=='s' :
            break;
        print('Enter one of r,p,s,q :')
    if move=='r':
        print('ROCK VS. ')
    elif move=='p':
        print('PAPER VS. :')
    elif move=='s':
        print('SCISSORS VS. :')
    computermove = ''
    randnum = 0
    print(randnum)
    randnum == random.randint(0,3)
    print(randnum)
    if randnum == 1:
        computermove ='r'
        print('ROCK')
    elif randnum == 2:
        computermove == 'p'
        print('PAPER')
    elif randnum == 3:
        computermove ='s'
        print('SCISSORS')

    if move==computermove:
        ties=ties+1
        print('its a tie!')
    elif move =='r' and computermove == 'p':
        print('You lost! ')
        lossess+=1
    elif move == 'r' and computermove=='s':
        print('You won!')
        wins+=1
    elif move=='p' and computermove == 'r':
        print('you won! ')
        wins+=1
    elif move == 'p' and computermove=='s':
        print('you lost!')
        lossess+=1
    elif move=='s' and computermove=='r':
        print('you lost!')
        lossess+=1
    elif move=='s' and computermove == 'p':
        print('you won!')
        wins+=1
