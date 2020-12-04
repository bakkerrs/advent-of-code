import re

# Credit: [kurocon/AdventOfCode202] helped me with the lambda functions, thanks!

def get_input():
    with open("./2020/4/input.txt") as f:
        input = f.read().split("\n\n")
        input = [x.replace("\n", " ") for x in input]
        input = [x.split(" ") for x in input]
        input = [dict(s.split(':') for s in x) for x in input]
        return input

"""
Requirements
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

requirements = {
    "byr": lambda x: int(x) and len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: int(x) and len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: int(x) and len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": lambda x: int(x[:-2]) and (
        (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
        (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76)
    ),
    "hcl": lambda x: len(x) == 7 and re.match("#[0-9a-f]{6}", x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: int(x) and len(x) == 9
}

def part1(input):
    count = 0
    for passport in input:
        for field in requirements.keys():
            if field not in passport.keys():
                break
        else:
            count += 1
    return count

def part2(input):
    count = 0
    for passport in input:
        for field, validator in requirements.items():
            if field not in passport.keys():
                break
            try:
                if not validator(passport[field]):
                    break
            except ValueError:
                break
        else:
            count += 1
    return count

def main():
    input = get_input()
    print(part1(input))
    print(part2(input))

main()