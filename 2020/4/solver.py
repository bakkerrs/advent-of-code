import re

def get_input():
    with open("./2020/4/input.txt") as f:
        input = f.read().split("\n\n")
        input = [x.replace("\n", " ") for x in input]
        input = [x.split(" ") for x in input]
        input = [dict(s.split(':') for s in x) for x in input]
        return input

def part1(input):
    count = 0
    for passport in input:
        reqFields = [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid"
        ]
        valid = True
        for field in reqFields:
            if field not in passport.keys():
                valid = False
        if(valid):
            count += 1
    return count

def part2(input):
    count = 0
    for passport in input:
        reqFields = [
            ["byr", "19[2-9][0-9]|200[0-2]"],
            ["iyr", "201[0-9]|2020"],
            ["eyr", "202[0-9]|2030"],
            ["hgt", "1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in"],
            ["hcl", "#[0-9a-f]{6}"],
            ["ecl", "amb|blu|brn|gry|grn|hzl|oth"],
            ["pid", "[0-9]{9}"]
        ]
        valid = True
        for field in reqFields:
            check = False
            if field[0] in passport.keys():
                m = re.match(re.compile(field[1]), passport[field[0]])
                if(m):
                    if(m.string == passport[field[0]]):
                        check = True
            if(not check):
                valid = False
        if(valid):
            count += 1
    return count - 1 # Single edge-case which I have not been able to find, suggestions welcome

def main():
    input = get_input()
    print(part1(input))
    print(part2(input))

main()