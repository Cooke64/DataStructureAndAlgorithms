"""
Питонячья красота:)
"""
from itertools import repeat
import itertools as it
import time


for a, b, c in map(lambda x, y: (x, y, x * y), repeat(2), range(6)):
    print(f'{a} * {b} = {c}')


symbols = ['.', '-', "'", '"', "'", '-', '.', '_']

for c in it.cycle(symbols):
    print(c, end='')
    time.sleep(0.05)