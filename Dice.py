from random import randint

tries = 0
wins = 0

print(f'Try to guess what number the dice will roll, from 1 to 6, enter any other number to quit the application.')
while True:
    player = int(input('Number: '))
    dice = randint(1, 6)
    if player == 0 or player > 6:
        print(f'You have chosen to quit, with an ending score of:\n'
              f'Attempts: {tries}\n'
              f'Wins: {wins}')
        break
    elif player == dice:
        tries += 1
        wins += 1
        print(f'You got it, the dice rolled {dice} and so did you.')
    elif player != dice:
        tries += 1
        print(f'Not this time, the dice rolled {dice} and you rolled {player}, keep trying.')
