def get_input():
    with open("./2022/day 01/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
def part1(input): 
    max = 0
    current_sum = 0
    for i in input:
        if i == "":
            if current_sum > max:
                max = current_sum
            current_sum = 0
        else:
            current_sum += int(i)
    
    return max
        



# Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def part2(input):
    calories = []
    current_sum = 0

    for mealCalories in input:
        if mealCalories == "":
            calories.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(mealCalories)
    
    calories.sort(reverse=True)

    total = 0
    for i in range(3):
        total += calories[i]

    return total

def main():
    print(part1(get_input()))
    print(part2(get_input()))



    pass

main()