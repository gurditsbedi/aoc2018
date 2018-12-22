
TEST_INPUT = open('./input.txt', 'r').readlines()
SAMPLE_INPUT = open('./sample.txt', 'r').readlines()


def parse(inp):
    initialState = list(inp[0].split()[-1])
    rules = {}

    for rule in inp[2:]:
        l = rule.split()
        rules[l[0]] = l[-1]

    return initialState, rules


def pgen(generation, centre):
    gen = ''.join(generation)
    c = centre - 3
    if c == 0:
        return gen
    elif c > 0:
        return gen[c:]
    else:
        return '.' * abs(c) + gen


def solve(initialState, rules):
    # initialState, rules = parse()

    sides = ['.', '.', '.']

    initialState = sides + initialState + sides
    nextState = ['.' for i in range(len(initialState))]

    total_pots = 0
    pots_increased = 0
    startLabel = 3

    for gen in range(100):

        if gen == 20:  # part1
            part1 = sum([i - startLabel  for i, x in enumerate(initialState) if x == '#'])

        pots_increased = initialState.count('#')
        total_pots += pots_increased

        for fl in range(2, len(initialState) - 2):
            flsurr = ''.join(initialState[fl-2:fl+3])
            if flsurr in rules:
                nextState[fl] = rules[flsurr]
            else:
                nextState[fl] = '.'

        initialState = nextState

        left_hash_index = initialState.index('#')
        if left_hash_index < 3:
            initialState = ['.' for i in range(3-left_hash_index)] + initialState
            startLabel = (3-left_hash_index) + startLabel
        elif left_hash_index > 3:
            initialState = initialState[left_hash_index-3:]
            startLabel = startLabel - (left_hash_index-3)

        right_hash_index_from_right = initialState[::-1].index('#')
        if right_hash_index_from_right < 3:
            initialState = initialState + ['.' for i in range(3-right_hash_index_from_right)]
        elif right_hash_index_from_right > 3:
            initialState = initialState[:right_hash_index-3]

        nextState = ['.' for i in range(len(initialState))]
        # print(f'{gen+1:2d} {pgen(initialState, startLabel)}')

    # part 2
    ans = sum([i - startLabel  for i, x in enumerate(initialState) if x == '#'])
    part2 = ans + (50000000000 - 100)*pots_increased

    # regresion
    return part1, part2


def main():
    # sample testing
    sample_parsed = parse(SAMPLE_INPUT)

    part1, _ = solve(*sample_parsed)

    assert part1 == 325

    # input testing
    input_parsed = parse(TEST_INPUT)
    part1, part2 = solve(*input_parsed)

    print('part1:', part1)
    print('part2:', part2)

    # regression
    assert part1 == 2571
    assert part2 == 3100000000655


main()
