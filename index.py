import random

print('Welcome to Rock Paper Scissors game !')

print('[ Game Options ]:')
print('1: Play with computer')
print('2: Play with other person')

option_choice = input('[Please enter your choice ]:')

print('OPTIONS: [rock, paper, scissors]')

if option_choice == '1':

    choices = ['rock', 'paper', 'scissors']
    random_num = random.randint(0,2)
    player_1_choice = input('[ enter Player 1\'s choice ]: ').lower()
    player_2_choice = choices[random_num]

    print(f'Player2 (Computer) chose {player_2_choice}')
else:
    player_1_choice = input('[ enter Player 1\'s choice ]: ').lower()
    player_2_choice = input('[ enter Player 2\'s choice ]: ').lower()


if player_1_choice == player_2_choice:
    print('Draw !')
elif player_1_choice == 'rock' and player_2_choice != 'paper':
    print('Player1 wins !')
elif player_1_choice == 'scissors' and player_2_choice == 'paper':
    print('Player1 wins !')
elif player_1_choice == 'paper' and player_2_choice == 'rock':
    print('Player1 wins !')
else:
    print('Player2 wins !')