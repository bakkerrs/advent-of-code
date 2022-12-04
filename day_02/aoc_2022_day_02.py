# Advent of Code 2022
# Day 02
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
        return [l.strip() for l in raw_input.readlines()]


def part_1(input_data: list):
    """Solution code for Part 1. Should return the solution."""
    WIN = 6
    DRAW = 3
    LOSE = 0
    
    shapes = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }

    shapeScore = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    result = {
        "rock": {
            "rock": DRAW,
            "paper": LOSE,
            "scissors": WIN
        },
        "paper": {
            "rock": WIN,
            "paper": DRAW,
            "scissors": LOSE
        },
        "scissors": {
            "rock": LOSE,
            "paper": WIN,
            "scissors": DRAW
        }
    }

    score = 0

    for round in input_data:
        opponent, you = round.split(" ")
        opponent = shapes[opponent]
        you = shapes[you]
        score += shapeScore[you] + result[you][opponent]

    return score


def part_2(input_data: list):
    """Solution code for Part 2. Should return the solution."""
    WIN = 6
    DRAW = 3
    LOSE = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    shapes = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSORS
    }

    outcomes = {
        "X": LOSE,
        "Y": DRAW,
        "Z": WIN
    }

    playedShape = {
        ROCK: {
            WIN: PAPER,
            DRAW: ROCK,
            LOSE: SCISSORS
        },
        PAPER: {
            WIN: SCISSORS,
            DRAW: PAPER,
            LOSE: ROCK
        },
        SCISSORS: {
            WIN: ROCK,
            DRAW: SCISSORS,
            LOSE: PAPER
        }
    }

    score = 0
    for round in input_data:
        opponent, outcome = round.split(" ")
        opponent = shapes[opponent]
        outcome = outcomes[outcome]
        score += playedShape[opponent][outcome] + outcome

    return score


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
