import re
from collections import namedtuple

SIDE = 1000
RAW = open("./input.txt", "r")
INPUT = [tuple(map(int, re.match(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', line).groups())) for line in RAW]


def solve():
    claim = namedtuple('claim', 'id x y w h')
    fabric = [[0 for _ in range(SIDE)] for _ in range(SIDE)]

    claims = []

    for c in INPUT:
        claims.append(claim(*c))

    for claim in claims:
        for i in range(claim.x, claim.x + claim.w):
            for j in range(claim.y, claim.y + claim.h):
                fabric[i][j] += 1

    count = 0
    for i in range(SIDE):
        for j in range(SIDE):
            if fabric[i][j] > 1:
                count += 1

    print('part1:', count)

    for cl in claims:
        if all([fabric[i][j] == 1 for i in range(cl.x, cl.x + cl.w) for j in range(cl.y, cl.y + cl.h)]):
            print('part2:', cl.id)



solve()
