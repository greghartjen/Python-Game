from random import randint

game_running = True
game_results = []


def calculate_enemy_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)


def game_ends(winner_name):
    print(f'{winner_name} won the game!')


while game_running:
    counter = 0
    new_round = True
    player = {'name': 'Greg', 'health': 100, 'attack': 13, 'heal': 16}
    enemy = {'name': 'Joe', 'health': 100, 'attack_min': 10, 'attack_max': 20}

    print('---' * 7)
    print('Enter Player Name:')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health.')
    print(enemy['name'] + ' has ' + str(enemy['health']) + ' health.')

    while new_round:

        counter = counter + 1
        player_won = False
        enemy_won = False

        print('---' * 7)
        print('Please select a move!')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Player Scores')

        player_choice = input()

        if player_choice == '1':
            enemy['health'] = enemy['health'] - player['attack']
            if enemy['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_enemy_attack(enemy['attack_min'], enemy['attack_max'])
                if player['health'] <= 0:
                    enemy_won = True
        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_enemy_attack(enemy['attack_min'], enemy['attack_max'])
            if player['health'] <= 0:
                enemy_won = True
        elif player_choice == '3':
            new_round = False
            game_running = False
        elif player_choice == '4':
            for player_stat in game_results:
                print(player_stat)
        else:
            print('Invalid input!')

        if player_won == False and enemy_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left.')
            print(enemy['name'] + ' has ' + str(enemy['health']) + ' left.')
        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
        elif enemy_won:
            game_ends(enemy['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False





