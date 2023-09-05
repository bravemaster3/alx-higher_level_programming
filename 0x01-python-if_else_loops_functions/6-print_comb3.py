#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x+1, 10):
        if (x == 8 and y == 9):
            print(f'{x:d}{y:d}')
        elif (x != y):
            print(f'{x:d}{y:d}, ', end='')
