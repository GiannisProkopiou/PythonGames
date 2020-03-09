import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
rows, cols = [int(i) for i in input().split()]
no_jumps = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

next_y = y0
next_x = x0

random.seed(a=None, version=2)

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    for times in range(no_jumps):

        if (bomb_dir == 'R'):
            next_y = next_y
            next_x = next_x + random.randint(1, rows - next_x)

            print(next_x, next_y)

        if (bomb_dir == 'L'):
            next_y = next_y
            next_x = next_x - random.randint(0, next_x - 1)

            print(next_x, next_y)

        if (bomb_dir == 'U'):
            next_y = next_y - random.randint(0, next_y - 1)
            next_x = next_x

            print(next_x, next_y)

        if (bomb_dir == 'D'):
            next_y = next_y + random.randint(0, cols - next_y - 1)
            next_x = next_x

            print(next_x, next_y)

        if (bomb_dir == 'UR'):
            next_y = next_y - random.randint(0, next_y)
            next_x = next_x + random.randint(0, rows - next_x - 1)

            print(next_x, next_y)

        if (bomb_dir == 'DR'):
            next_y = next_y + random.randint(0, cols - next_y + 1)
            next_x = next_x + random.randint(0, rows - next_x - 1)

            print(next_x, next_y)

        if (bomb_dir == 'DL'):
            next_y = next_y + random.randint(0, cols - next_y + 1)
            next_x = next_x - random.randint(0, next_x - 1)

            print(next_x, next_y)

        if (bomb_dir == 'UL'):
            next_y = next_y - random.randint(0, next_y)
            next_x = next_x - random.randint(0, next_x)

            print(next_x, next_y)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # the location of the next window Batman should jump to.