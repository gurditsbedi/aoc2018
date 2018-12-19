with open('./input.txt', 'r') as f:
    nums = [int(line.strip()) for line in f]
    sumOfNums = sum(nums)
    print(f'part1: {sumOfNums}')

    seen = set()
    total = 0
    find = False
    while True:
        for n in nums:
            total += n
            if total in seen:
                print('part2:', total)
                find = True
                break
            seen.add(total)
        if find:
            break


    # print(seen)
    # print(len(seen))
