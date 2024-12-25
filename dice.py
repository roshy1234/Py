import random as r

def roll():
    min_value = 1
    max_value = 6
    values = r.randint(1,6)
    return values

#number of players
while True:
    players = input('Enter the number of players (2-4) : ')
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4 :
            break
        else:
            print('No. of players between 2 and 4!')
    else:
        print('Invalid!, Try Again')

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) <= max_score: #game until one player reaches max score
    for p in range(players): #turn for each player
        print(f'player {p+1} chance')
        curr_score = 0
        while True:
            should_roll = input("Do you want to roll again (y)? ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done!')
                curr_score = 0
                break
            else:
                curr_score += value
                print(f'You rolled a : {value}')

            print(f'Your score is {curr_score}')

        player_score[p] += curr_score
        print(f'Your total score is : {player_score[p]}')

for p in range(players):
    if player_score[p] >= max_score:
        print(f'Player {p+1} won')
