
TEST_INPUT = open('./input.txt').readline().rsplit()[0]


def reactable(chx, chy):
    return chx != chy and chx.lower() == chy.lower()


def solve_part1(polymer):
    p = list(polymer)

    i = 0
    while True:
        if i > len(p)-2:
            break
        if reactable(p[i], p[i + 1]):
            del p[i+1]
            del p[i]
            i = 0 if i - 1 < 0 else i - 1
        else:
            i += 1

    return len(p)


def solve_part2(polymer):
    orip = list(polymer)
    letters = "abcdefghijklmnopqrstuvwxyz"

    min_letter = ''
    min_value = len(orip) + 1

    for letter in letters:
        p = [r for r in orip if r != letter and r != letter.upper()]
        i = 0
        while True:
            if i > len(p) - 2:
                break
            if reactable(p[i], p[i + 1]):
                del p[i + 1]
                del p[i]
                i = 0 if i - 1 < 0 else i - 1
            else:
                i += 1

        if len(p) < min_value:
            min_value = len(p)
            min_letter = letter

    return min_value


assert solve_part1('dabAcCaCBAcCcaDA') == 10
assert solve_part2('dabAcCaCBAcCcaDA') == 4

part1 = solve_part1(TEST_INPUT)
print('part1: ', part1)
part2 = solve_part2(TEST_INPUT)
print('part2: ', part2)

# regression
assert part1 == 10888
assert part2 == 6952
