def get_input():
    with open("./2020/2/input.txt") as f:
        return f.read().split("\n")

def split_input(input):
    policy, password = [x.strip() for x in input.split(":")]
    bounds, token = policy.split(" ")
    lower, upper = [int(x) for x in bounds.split("-")]
    return(lower, upper, token, password)

def part1(input):
    i = 0
    for x in input:
        lower, upper, token, password = split_input(x)
        count = password.count(token)
        if(count >= lower and count <= upper):
            i += 1
    print(i)

def part2(input):
    i = 0
    for x in input:
        lower, upper, token, password = split_input(x)
        a = password[lower-1]
        b = password[upper-1]
        if((a == token) ^ (b == token)):
            i += 1
    
    print(i)

def main():
    part1(get_input())
    part2(get_input())
    pass

main()