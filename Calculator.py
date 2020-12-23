from math import pow
from math import factorial
from math import sqrt

# This is a practice code, may you have any tips on how to make the code cleaner, better, shorter, let me know.

n1 = None
n2 = None
result = None
choice = None

print(f'Welcome to the calculator.')
print('-'*26)

while True:
    print('Choose one of the options below or enter 0 to quit.')
    print('[1] - Addition\n'
          '[2] - Subtraction\n'
          '[3] - Multiplication\n'
          '[4] - Division\n'
          '[5] - Exponentiation\n'
          '[6] - Factorial\n'
          '[7] - Square root\n'
          '[0] - Quit')
    choice = int(input('Command: '))
    if choice == 1:
        n1 = float(input('Number 1: '))
        n2 = float(input('Number 2: '))
        result = n1 + n2
        print(f'{n1} + {n2} = {result}')
    elif choice == 2:
        n1 = float(input('Number 1: '))
        n2 = float(input('Number 2: '))
        result = n1 - n2
        print(f'{n1} - {n2} = {result}.')
    elif choice == 3:
        n1 = float(input('Number 1: '))
        n2 = float(input('Number 2: '))
        result = n1 * n2
        print(f'{n1} * {n2} = {result}.')
    elif choice == 4:
        n1 = float(input('Number 1: '))
        n2 = float(input('Number 2: '))
        try:
            result = n1 / n2
        except ZeroDivisionError:
            print(f'It is not possible to divide a number by 0, please try again.')
        else:
            print(f'{n1} / {n2} = {result}.')
    elif choice == 5:
        n1 = float(input('Number 1: '))
        n2 = float(input('Number 2: '))
        result = pow(n1, n2)
        print(f'{n1} ^ {n2} = {result}.')
    elif choice == 6:
        n1 = float(input('Number: '))
        result = factorial(n1)
        print(f'{n1}! = {result}')
    elif choice == 7:
        n1 = float(input('Number: '))
        result = sqrt(n1)
        print(f'√{n1} = {result}')
    elif choice == 0:
        break
    print('Thank you for using me, may you have any feedback or tip on how to improve the code, please let me know.')


