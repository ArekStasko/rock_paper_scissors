print('Welcome to Rock Paper Scissors game !')
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