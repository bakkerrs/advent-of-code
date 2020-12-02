def get_input():
    with open("./2020/1/input.txt") as f:
        return [int(x.strip()) for x in f.read().split("\n")]

# Part 1: Find the two entries that sum to 2020 and multiply them by eachother
def part1(input): 
    for i in input:
        for j in input:
            if(i + j == 2020):
                return(i*j)

# Part 2: Find the three entries that sum to 2020 and multiply them by eachother
def part2(input):
    for i in input:
        for j in input:
            for k in input:
                if(i + j + k == 2020):
                    return(i*j*k)

def main():
    print(part1(get_input()))
    print(part2(get_input()))
    pass

main()