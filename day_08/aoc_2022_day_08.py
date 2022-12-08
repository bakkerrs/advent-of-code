# Advent of Code 2022
# Day 08
# Robin Bakker

import argparse
import logging
import sys

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

        input = [[int(x) for x in y.strip()] for y in raw_input.readlines()]

        forest = [
            [
                {
                    "height": h,
                    "visibility": {
                        "up": None,
                        "down": None,
                        "left": None,
                        "right": None,
                    },
                    "viewing_distance": {
                        "up": None,
                        "down": None,
                        "left": None,
                        "right": None,
                    },
                    "visible": None,
                    "scenic_score": None,
                }
                for h in x
            ]
            for x in input
        ]

        def next_tree(x, y, direction):
            edge = False
            nextx, nexty = x, y
            match direction:
                case "left":
                    if x == 0:
                        edge = True
                    else:
                        nextx -= 1

                case "right":
                    if x == len(forest[y]) - 1:
                        edge = True
                    else:
                        nextx += 1
                case "up":
                    if y == 0:
                        edge = True
                    else:
                        nexty -= 1
                case "down":
                    if y == len(forest) - 1:
                        edge = True
                    else:
                        nexty += 1
            return [edge, nextx, nexty]

        def visible(x, y, direction):
            if forest[y][x]["visibility"][direction] is not None:
                return forest[y][x]["visibility"][direction]

            edge, nextx, nexty = next_tree(x, y, direction)
            height = forest[y][x]["height"]
            if edge:
                forest[y][x]["visibility"][direction] = [True, height]
            else:
                visibleheight_neighbour = visible(nextx, nexty, direction)[1]
                if visibleheight_neighbour >= forest[y][x]["height"]:
                    forest[y][x]["visibility"][direction] = [
                        False,
                        visibleheight_neighbour,
                    ]
                else:
                    forest[y][x]["visibility"][direction] = [True, height]

            return forest[y][x]["visibility"][direction]

        def viewing_distance(x, y, direction, considering, considered_height=0):
            view = None

            edge, nextx, nexty = next_tree(x, y, direction)
            height = forest[y][x]["height"]
            if edge:
                view = 0
            elif forest[nexty][nextx]["height"] < considered_height and not considering:
                view = (
                    viewing_distance(nextx, nexty, direction, False, considered_height)
                    + 1
                )
            elif forest[nexty][nextx]["height"] < height and considering:
                view = viewing_distance(nextx, nexty, direction, False, height) + 1
            else:
                view = 1
            if considering:
                forest[y][x]["viewing_distance"][direction] = view
            return view

        for y in range(0, len(forest)):
            for x in range(0, len(forest[y])):
                score = 1
                for direction in ["up", "down", "left", "right"]:
                    if visible(x, y, direction)[0]:
                        forest[y][x]["visible"] = True
                    score *= viewing_distance(x, y, direction, True)
                if forest[y][x]["visible"] is None:
                    forest[y][x]["visible"] = False
                forest[y][x]["scenic_score"] = score

        return forest


def part_1(forest: list):
    """Solution code for Part 1. Should return the solution."""
    sum = 0
    for y in forest:
        for tree in y:
            if tree["visible"]:
                sum += 1

    return sum


def part_2(forest: list):
    """Solution code for Part 2. Should return the solution."""
    max = 0
    for y in forest:
        for tree in y:
            if tree["scenic_score"] > max:
                max = tree["scenic_score"]
    return max


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
