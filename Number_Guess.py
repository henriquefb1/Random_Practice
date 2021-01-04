from random import randint

print(f'Welcome! You will have 15 chances to guess which number I am thinking of.\n'
      f'It will be a number between 1-50 and after each try I will let you know if you need to go higher or lower. \n'
      f'You will be able to quit the application at any moment by entering any number outside the range 1-50.')

number = randint(1, 50)
tries = 0
victory = 0
print(f'So, I have thought of a number, it is set, now it is your turn!')
for x in range(1, 16):
    attempt = int(input('Try it: '))
    if attempt < 1 or attempt > 50:
        print(f'You have chosen to quit the application, thank you for playing with me.')
        break
    elif attempt < number:
        print(f'You have entered a number lower than expected, try higher.')
        tries += 1
    elif attempt > number:
        print(f'Ops, too high, try guessing a lower number!')
        tries += 1
    elif attempt == number:
        tries += 1
        victory = 1
        print(f'There you go! {number} is what I was thinking of! Great job\n'
              f'You have done it in {tries} attempts.')
if victory == 0:
    print(f'Seems like you have spent all your 15 chances, better luck next time!\n'
          f'The number I was thinking of is {number}.')