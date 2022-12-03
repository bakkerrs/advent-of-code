def get_input():
    with open("./2022/day 03/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# Part 1: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
def part1(input): 
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    for rucksack in input:
        first_compartment = rucksack[0:int(len(rucksack)/2)]
        second_compartment = rucksack[int(len(rucksack)/2):int(len(rucksack))]
        
        for item in first_compartment:
            if item in second_compartment:
                common_item = item
                break

        sum_priorities += items.index(common_item) + 1
    
    return sum_priorities

        
# Part 2: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
def part2(input):
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum_priorities = 0
    group = []
    for rucksack in input:
        group.append(rucksack)

        if len(group) == 3:
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    badge = item
                    break
            
            sum_priorities += items.index(badge) + 1
            group = []
    
    return sum_priorities

def main():
    print(part1(get_input()))
    print(part2(get_input()))

    pass

main()