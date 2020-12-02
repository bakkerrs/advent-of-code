import re

def get_input():
    with open("./2020/2/input.txt") as f:
        return f.read().split("\n")

def split_input(input):
    # Takes input (e.g. 2-3 n: nnjn) and splits it into it's components
    lower, upper, token, password = re.split("[- :]+", input)
    return(int(lower), int(upper), token, password)

def part1(input):
    i = 0
    for x in input:
        # Count amount of times the password fulfills the password requirements
        # Amount of times token exists in passwords needs te be between lower and upper bounds
        lower, upper, token, password = split_input(x)
        count = password.count(token)
        if(count >= lower and count <= upper):
            i += 1
    return(i)

def part2(input):
    i = 0
    for x in input:
        # Count amount of times the password fulfills the password requirements
        # Character in position a or b needs to equal token exactly once. (XOR)
        lower, upper, token, password = split_input(x)
        a = password[lower-1]
        b = password[upper-1]
        if((a == token) ^ (b == token)):
            i += 1
    return(i)

def main():
    print(part1(get_input()))
    print(part2(get_input()))
    pass

main()