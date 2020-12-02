import re

def get_input():
    with open("./2020/2/input.txt") as f:
        return f.read().split("\n")

def split_input(input):
    lower, upper, token, password = re.split("[- :]+", input)
    return(int(lower), int(upper), token, password)

def part1(input):
    i = 0
    for x in input:
        lower, upper, token, password = split_input(x)
        count = password.count(token)
        if(count >= lower and count <= upper):
            i += 1
    return(i)

def part2(input):
    i = 0
    for x in input:
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