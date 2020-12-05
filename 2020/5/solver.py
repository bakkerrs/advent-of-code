def get_input():
    with open("./2020/5/input.txt") as f:
        return f.read().split("\n")

def get_id(boardingpass, lower, upper):
    for x in boardingpass:
        if x == "B" or x == "R":
            lower = lower + (upper - lower + 1) / 2
        if x == "F" or x == "L":
            upper = lower + (upper - lower + 1) / 2 - 1
    return upper

def check_pass(boardingpass):
    row = get_id(boardingpass[:7], 0, 127)
    seat = get_id(boardingpass[-3:], 0, 7)
    return row * 8 + seat

def part1(passes):
    max_id = 0
    for boardingpass in passes:
        seatid = check_pass(boardingpass)
        if max_id < seatid:
            max_id = seatid
    return max_id

def part2(passes): 
    seatids = [check_pass(x) for x in passes]
    seatids.sort()
    for i in range(0, len(seatids)-2):
        if(seatids[i] == seatids[i+1]-2):
            return seatids[i]+1

def test():
    assert check_pass("BFFFBBFRRR") == 567
    assert check_pass("FFFBBBFRRR") == 119
    assert check_pass("BBFFBBFRLL") == 820

def main():
    test()
    passes = get_input()
    print(part1(passes))
    print(part2(passes))

main()