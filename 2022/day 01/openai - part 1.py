def input():
    with open("./2022/day 01/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# The list of Elves and their Calories
elves = {}

# Read the input
current_elf = None
id = 0
for line in input():
  try:
    if line == "":
      # Start a new Elf
      current_elf = None
    elif current_elf is None:
      # Start a new Elf with the given name
      id += 1
      current_elf = id
      elves[current_elf] = int(line)
    else:
      # Add the Calories to the current Elf
      elves[current_elf] += int(line)
  except EOFError:
    # End of input, stop reading
    break

# Find the Elf with the most Calories
max_calories = 0
max_elf = None
for elf, calories in elves.items():
  if calories > max_calories:
    max_calories = calories
    max_elf = elf

# Print the result
print("The Elf carrying the most Calories is", max_elf)
print("They are carrying", max_calories, "total Calories")
