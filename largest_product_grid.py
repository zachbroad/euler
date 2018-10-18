import os
import numpy
from functools import reduce

grid_data = None

with open('20x20.txt', 'r') as grid:
    grid_data = grid.read().split(',')


# rows = []
# for key, row in enumerate(range(0, 20*20, 20)):
#     rows.append(grid_data[row:row+20])


# (y, x) => (2, 2) => 3rd row, 3rd column
# ()
# UP (1, 0) -   (2, 2) => (3, 2)
# DOWN (0, 1) - (2, 2) => (1, 2)
# LEFT (2, 2) => (2, 1)
# RIGHT (2, 2) => (2, 3)


def get_four_numbers(key, vector):
    numbers = []

    for i in range(4):
        try:
            numbers.append(int(grid_data[int(key) + (i * vector)]))
        except:
            return None

    if len(numbers) == 4:
        return numbers
    else:
        return None

    # get four numbers; return as list
    # else; return None


VECTOR = {
    'UP': -20,  # -20
    'DOWN': 20,  # +20
    'LEFT': -1,  # -1
    'RIGHT': 1,  # +1
    'UR': -19,
    'UL': -21,
    'DR': 21,
    'DL': 19,
}


def compute():
    products = []
    highest_product = 1
    for key, number in enumerate(grid_data):
        for direction, magnitude in VECTOR.items():
            numbers = get_four_numbers(key, magnitude)

            if numbers is not None:
                product = reduce(lambda x, y: x*y, numbers)
                highest_product = product if product > highest_product else highest_product

    print('SOLUTION: ', highest_product)


import time
start = time.time()
compute()
end = time.time()
print(end-start, ' seconds')
