# Advent of Code 2022
# Day 09
# Robin Bakker

import argparse
import logging
import sys
import numpy as np

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
        return [l.strip().split() for l in raw_input.readlines()]


def chase(me, them):
    stepx = them[0] - me[0]
    stepy = them[1] - me[1]
    if np.abs(stepx) <= 1 and np.abs(stepy) <= 1:
        return me
    else:
        move = np.sign([stepx, stepy])
        return np.add(me, move)


def move(positions, dir):
    directions = {
        "U": np.array([0, 1]),
        "D": np.array([0, -1]),
        "R": np.array([1, 0]),
        "L": np.array([-1, 0]),
    }
    positions[0] = np.add(positions[0], directions[dir])
    for j in range(1, len(positions)):
        positions[j] = chase(positions[j], positions[j - 1])
    return positions


def mark_visited(grid, pos):
    if pos[1] not in grid:
        grid[pos[1]] = {}
    if pos[0] not in grid[pos[1]]:
        grid[pos[1]][pos[0]] = True
        return [grid, True]
    return [grid, False]


def process(actions, positions):
    grid = {0: {0: True}}
    sum = 1
    for dir, amount in actions:
        for i in range(int(amount)):
            positions = move(positions, dir)
            grid, new = mark_visited(grid, positions[-1])
            if new:
                sum += 1
    return sum


def part_1(actions: list):
    """Solution code for Part 1. Should return the solution."""

    return process(actions, [np.array([0, 0])] * 2)


def part_2(actions: list):
    """Solution code for Part 2. Should return the solution."""

    return process(actions, [np.array([0, 0])] * 10)


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    input = parse_input(SAMPLE_PATH)
    print(part_1(input))


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
