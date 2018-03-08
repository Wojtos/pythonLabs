#!/usr/local/bin/python3
import random;

while True:
    try:
        minNumber = input('Podaj minimalna liczbe\n')
        maxNumber = input('Podaj maksymalna liczbe\n')
        ourNumber = random.randint(int(minNumber), int(maxNumber))
        break
    except ValueError as error:
        print(error)

finnished = False

while not finnished:
    try:
        userNumber = int(input('Podaj liczbe\n'))
        if userNumber == ourNumber:
            print('Odgadles liczbe')
            finnished = True
        elif userNumber > ourNumber:
            print('Podaj mniejsza liczbe!')
        else:
            print('Podaj wieksza liczbe!')
    except ValueError as error:
        print(error)
