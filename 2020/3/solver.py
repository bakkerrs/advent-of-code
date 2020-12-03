def get_input():
    with open("./2020/3/input.txt") as f:
        return f.read().split("\n")
    
def main():
    map = get_input()
    print(part1(map))
    print(part2(map))

def check_slope(map, slope):
    x = 0
    y = 0
    trees = 0
    width = len(map[0])
    height = len(map)
    while y < height:
        if(map[y][x%width] == "#"):
            trees += 1
        x += slope[0]
        y += slope[1]
    return trees

def part1(map):
    slope = [3, 1]
    return check_slope (map, slope)

def part2(map):
    # Slopes (right, down)
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    output = 1
    for slope in slopes:
        output *= check_slope(map, slope)
    return output

main()