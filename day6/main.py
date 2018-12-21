from collections import namedtuple, defaultdict

TEST_INPUT = open('./input.txt').readlines()
SAMPLE_INPUT = open('./sample.txt').readlines()

Point = namedtuple('Point', 'x y')


def mdist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def parseInput(inp):
    return [Point(*tuple(map(int, x.split(',')))) for x in inp]


def solve_part1(points):
    count = defaultdict(int)
    infinite = set()

    topleft = Point(min(p.x for p in points), min(p.y for p in points))
    bottomright = Point(max(p.x for p in points), max(p.y for p in points))

    for y in range(topleft.y, bottomright.y + 1):
        for x in range(topleft.x, bottomright.x + 1):
            distances = sorted(((mdist(p, Point(x, y)), idx) for idx, p in enumerate(points)))

            if distances[0][0] != distances[1][0]:
                count[distances[0][1]] += 1

                if y in (topleft.y, bottomright.y) or x in (topleft.x, bottomright.x):
                    infinite.add(distances[0][1])

    for inf in infinite:
        count.pop(inf)

    return max(count.values())


def solve_part2(points, limit):
    topleft = Point(min(p.x for p in points), min(p.y for p in points))
    bottomright = Point(max(p.x for p in points), max(p.y for p in points))

    count = 0
    for y in range(topleft.y, bottomright.y + 1):
        for x in range(topleft.x, bottomright.x + 1):
            dist_sum = sum(mdist(p, Point(x, y)) for p in points)

            if dist_sum < limit:
                count += 1

    return count


def solve():
    # SAMPLE_TESTING
    sample_parsed = parseInput(SAMPLE_INPUT)

    sample_part1 = solve_part1(sample_parsed)
    assert sample_part1 == 17

    sample_part2 = solve_part2(sample_parsed, 32)
    assert sample_part2 == 16

    # INPUT_TESTING
    test_parsed = parseInput(TEST_INPUT)

    part1 = solve_part1(test_parsed)
    print('part1:', part1)

    part2 = solve_part2(test_parsed, 10000)
    print('part2:', part2)

    # regression
    assert part1 == 4754
    assert part2 == 42344

solve()
