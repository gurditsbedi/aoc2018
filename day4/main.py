import re
from collections import defaultdict

TEST_INPUT = open('./input.txt').readlines()
SAMPLE_INPUT = open('./test.txt').readlines()

total_slept = defaultdict(int)
slept_at_minute = defaultdict(lambda: defaultdict(int))


def parseInput(timetable):
    for line in sorted(timetable):
        line = line.rstrip()
        nums = tuple(map(int, re.findall(r'\d+', line)))

        if len(nums) == 6:
            gid = nums[-1]
        elif len(nums) == 5:
            if 'asleep' in line:
                minute_fall = nums[-1]
            elif 'wakes' in line:
                minute_wake = nums[-1]

                total_slept[gid] += (minute_wake - minute_fall)
                for m in range(minute_fall, minute_wake):
                    slept_at_minute[gid][m] += 1

    return total_slept, slept_at_minute


def solve_part1():
    max_slept_gid = 0
    max_slept_mins = 0
    max_slept_at_min = 0

    for gid, mins in total_slept.items():
        if mins > max_slept_mins:
            max_slept_gid = gid
            max_slept_mins = mins

    t = 0
    for minute, times in slept_at_minute[max_slept_gid].items():
        if times > t:
            max_slept_at_min = minute
            t = times

    return max_slept_gid * max_slept_at_min


def solve_part2():
    minutes = defaultdict(lambda: defaultdict(int))
    # minutes = defaultdict(int)

    for gid, sleep_schedule in slept_at_minute.items():
        for minute, times in sleep_schedule.items():
            if times > minutes[minute]['times']:
                minutes[minute]['gid'] = gid
                minutes[minute]['times'] = times

    max_gid = 0
    max_min = 0
    times = 0
    for m, k in minutes.items():
        if minutes[m]['times'] > times:
            max_gid = minutes[m]['gid']
            max_min = m
            times = minutes[m]['times']

    return max_gid * max_min


# SAMPLE_TESTING
parseInput(SAMPLE_INPUT)

sample_part1 = solve_part1()
assert sample_part1 == 240

sample_part2 = solve_part2()
assert sample_part2 == 4455

# INPUT_TESTING
parseInput(TEST_INPUT)

part1 = solve_part1()
print('part1:', part1)

part2 = solve_part2()
print('part2:', part2)

# regression
assert part1 == 39584
assert part2 == 55053
