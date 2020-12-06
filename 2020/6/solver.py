from collections import Counter
import string

def get_input():
    with open("./2020/6/input.txt") as f:
        return f.read().split("\n\n")
         

def part1(groups):
    sum = 0
    for group in [x.replace("\n","") for x in groups]:
        sum += len(Counter(group).keys())
    return sum

def part2(groups):
    groups = [x.split("\n") for x in groups]
    sum = 0
    for group in groups:
        group = [Counter(x) for x in group]
        common = Counter(string.ascii_lowercase)
        for individual in group:
            common = common & individual
        sum += len(common)
    return sum

def main():
    groups = get_input()
    print(part1(groups))
    print(part2(groups))

main()
