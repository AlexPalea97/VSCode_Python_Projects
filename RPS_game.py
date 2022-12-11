import random

# 0 = sasso
# 1 = carta
# 2 = forbice

computer_score = 0
human_score = 0

options = ['sasso', 'carta', 'forbice']

game_matrix = [ 
    ['pari', 'computer', 'player'],
    ['player', 'pari', 'computer'],
    ['computer', 'player', 'pari']
]

game = True

while game:
    print('0 = sasso')
    print('1 = carta')
    print('2 = forbice')
    print('3 = resetta il risultato')
    print('4 = Fine del gioco')

    player_choice = input('\nChe cosa scegli?\n')

    if player_choice == '4':
        print('Gioco termianto')
        print(f'Giocatore: {human_score} \t Computer: {computer_score}')
        game = False
    elif player_choice == '3':
        print('Azzeramento dei punteggi')
        print(f'Giocatore: {human_score} \t Computer: {computer_score}')
        human_score = 0
        computer_score = 0
    elif int(player_choice) in range(0, 3):
        computer = random.randint(0, 2)
        player = int(player_choice)
        print(f'{options[player]} vs {options[computer]}')
        if game_matrix[player][computer] == 'computer':
            computer_score += 1
            print(f'Vince: {game_matrix[player][computer]}')
        elif game_matrix[player][computer] == 'player':
            human_score += 1
            print(f'Vince: {game_matrix[player][computer]}')
        else:
            print('Pareggio')
    else:
        print('Scelta non valida')

