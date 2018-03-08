#!/usr/local/bin/python3
import random;

minNumber = input('Podaj minimalna liczbe\n');
maxNumber = input('Podaj maksymalna liczbe\n');

try:
    print(random.randint(int(minNumber), int(maxNumber)));
except ValueError as error:
    print(error);
