# Advent of Code 2022
# Day 05
# Robin Bakker

import argparse
import logging
import sys
import re

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
        rawstacks, moves = [
            parts.split("\n") for parts in raw_input.read().split("\n\n")
        ]
        maxStack = int(rawstacks.pop().strip().split("   ")[-1])
        stacks = [[] for _ in range(maxStack)]
        for row in rawstacks:
            for i in range(1, maxStack * 4, 4):
                if row[i] != " ":
                    stacks[(i - 1) // 4].insert(0, row[i])

        moves = [[int(num) for num in re.findall(r"\d+", move)] for move in moves]

        return [stacks, moves]


def part_1(input_data: list):
    """Solution code for Part 1. Should return the solution."""

    stacks, moves = input_data

    for move in moves:
        amount, fromStack, toStack = move
        for i in range(amount):
            crate = stacks[fromStack - 1].pop()
            stacks[toStack - 1].append(crate)

    out = ""
    for stack in stacks:
        out += stack[-1]

    return out


def part_2(input_data: list):
    """Solution code for Part 2. Should return the solution."""
    stacks, moves = input_data

    for move in moves:
        amount, fromStack, toStack = move
        for i in range(amount):
            crate = stacks[fromStack - 1].pop(-amount + i)
            stacks[toStack - 1].append(crate)

    out = ""
    for stack in stacks:
        out += stack[-1]

    return out


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    print(parse_input(SAMPLE_PATH))


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
