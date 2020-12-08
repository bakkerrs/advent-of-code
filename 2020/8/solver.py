def get_input():
    with open("./2020/8/input.txt") as f:
        return f.read().split("\n")

def part1(instructions):
    return runprogram(instructions)

def runprogram(instructions, change = -1):
    pointer = 0
    acc = 0
    previous_pointers = []
    success = True
    while True and pointer < len(instructions):
        if pointer in previous_pointers:
            success = False
            break
        else:
            previous_pointers.append(pointer)

        operation, argument = instructions[pointer].split(" ")
        argument = int(argument)

        if pointer == change:
            if operation == "nop":
                operation = "jmp"
            if operation == "jmp":
                operation = "nop"

        if operation == "nop":
            pointer += 1
        if operation == "jmp":
            pointer += argument
        if operation == "acc":
            acc += argument
            pointer += 1
    return acc, success

def part2(instructions):
    for i in range(len(instructions)):
        if "jmp" in instructions[i]:
            acc, success = runprogram(instructions, i)
            if success:
                return acc, success
        if "nop" in instructions[i]:
            acc, success = runprogram(instructions, i)
            if success:
                return acc, success


def main():
    input = get_input()
    print(part1(input))
    print(part2(input))

main()