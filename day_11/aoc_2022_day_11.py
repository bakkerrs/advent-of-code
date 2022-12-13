# Advent of Code 2022
# Day 11
# Had to get help due to scaling issues. My code could not support 10000 rounds..
# thanks, @Kokopak

import argparse
import logging
import sys
import re
import operator

from pathlib import Path

PARENT_FOLDER = Path(__file__).parent
BASE_FILE_NAME = Path(__file__).stem
INPUT_FILE_NAME = f"{BASE_FILE_NAME}_input.txt"
SAMPLE_FILE_NAME = f"{BASE_FILE_NAME}_sample.txt"

INPUT_PATH = PARENT_FOLDER / INPUT_FILE_NAME
SAMPLE_PATH = PARENT_FOLDER / SAMPLE_FILE_NAME


logger = logging.getLogger("aoc_logger")
log_handler = logging.StreamHandler()
log_handler.setLevel("DEBUG")
logger.addHandler(log_handler)


# ---=== PROBLEM CODE BELOW ===---


def parse_input(data_path: Path) -> list:
    """
    Reads and formats input.
    Should return the input data in a format where it is ready to be worked on.
    """
    with open(data_path, "r") as raw_input:
        input = raw_input.read().split("\n\n")
        monkeys = []
        for s in input:
            regex = (
                r"Monkey (\d+):\n"
                r"  Starting items:([ \d+,]*)\n"
                r"  Operation: new = old (.) (.+)\n"
                r"  Test: divisible by (\d+)\n"
                r"    If true: throw to monkey (\d+)\n"
                r"    If false: throw to monkey (\d+)"
            )
            (
                monkey,
                items,
                operator,
                operator_value,
                divisible_by,
                true_monkey,
                false_monkey,
            ) = re.findall(regex, s)[0]

            monkeys.append(
                {
                    "items": list(map(int, items.split(","))),
                    "operator": MAP_SIGN[operator],
                    "operator_value": operator_value,
                    "divisible_by": int(divisible_by),
                    "if_true": int(true_monkey),
                    "if_false": int(false_monkey),
                    "inspected_items": 0,
                }
            )
        return monkeys


MAP_SIGN = {
    "+": operator.add,
    "*": operator.mul,
    "/": operator.truediv,
    "-": operator.sub,
}


def get_monkey_business(n, monkeys, small_number=False):
    total_modulo = 1
    for modulo in [int(monkey["divisible_by"]) for monkey in monkeys]:
        total_modulo *= modulo

    for _ in range(n):
        for monkey in range(len(monkeys)):
            for i in range(len(monkeys[monkey]["items"])):
                item = monkeys[monkey]["items"].pop(0)

                operator_value = monkeys[monkey]["operator_value"]
                operator_value = (
                    int(operator_value) if operator_value != "old" else item
                )

                divisible_by = int(monkeys[monkey]["divisible_by"])

                worry_level = monkeys[monkey]["operator"](item, operator_value)
                worry_level //= 3 if small_number else 1

                monkeys[monkey]["inspected_items"] += 1

                if worry_level % divisible_by == 0:
                    monkeys[monkeys[monkey]["if_true"]]["items"].append(
                        worry_level % total_modulo
                    )
                else:
                    monkeys[monkeys[monkey]["if_false"]]["items"].append(
                        worry_level % total_modulo
                    )

    inspected_items = [monkey["inspected_items"] for monkey in monkeys]

    return operator.mul(*sorted(inspected_items, reverse=True)[:2])


def part_1(monkeys: list):
    """Solution code for Part 1. Should return the solution."""

    return get_monkey_business(20, monkeys, True)


def part_2(monkeys: list):
    """Solution code for Part 2. Should return the solution."""

    return get_monkey_business(10000, monkeys, False)


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    print(part_2(parse_input(SAMPLE_PATH)))


# ---=== PROBLEM CODE ABOVE ===---


def problem_dispatch(mode: str, part: int, log_level: str = None):
    if log_level is not None:
        logger.setLevel(log_level.upper())
    parts = {1: part_1, 2: part_2}
    inputs = {"check": parse_input(SAMPLE_PATH), "solve": parse_input(INPUT_PATH)}
    return parts[part](inputs[mode])


def run_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", type=str, choices={"check", "solve"})
    parser.add_argument("part", type=int, choices={1, 2})
    parser.add_argument(
        "--log-level",
        type=str,
        required=False,
        choices={"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"},
    )
    args = parser.parse_args()
    print(problem_dispatch(args.mode, args.part, args.log_level))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit(run_direct())
    else:
        raise SystemExit(run_cli())
