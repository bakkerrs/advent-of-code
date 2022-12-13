# Advent of Code 2022
# Day 10
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
        out = []
        for i in [l.strip() for l in raw_input.readlines()]:
            if i == "noop":
                out.append([i, ""])
            else:
                instr, arg = i.split(" ")
                out.append([instr, int(arg)])
        return out


class Cycle:
    def __init__(self, cycle=1, x=1):
        self.cycle = cycle
        self.x = x
        self.sum = 0
        self.measurements = [20, 60, 100, 140, 180, 220]

    def checkSignal(self):
        if self.cycle in self.measurements:
            measurement = self.cycle * self.x
            print(
                "Measurement during cycle",
                self.cycle,
                "with x",
                self.x,
                " = ",
                measurement,
            )
            self.sum += measurement

    def noop(self):
        self.cycle += 1
        self.checkSignal()

    def addx(self, arg):
        self.cycle += 1
        self.checkSignal()
        self.cycle += 1
        self.x += arg
        self.checkSignal()

    def getSum(self):
        return self.sum


def part_1(input: list):
    """Solution code for Part 1. Should return the solution."""
    cycle = Cycle()

    for op, arg in input:
        match op:
            case "noop":
                cycle.noop()
            case "addx":
                cycle.addx(arg)

    return cycle.getSum()


class CRT:
    spritex = 0
    posy = 0

    def __init__(self, width: int, height: int):
        self.image = []
        for h in range(height):
            self.image.append("")
        self.width = width
        self.height = height

    def drawSprite(self):
        if len(self.image[self.posy]) == self.width:
            self.posy += 1

        if self.posy == self.height:
            pass

        if len(self.image[self.posy]) + 1 in range(self.spritex, self.spritex + 3):
            self.image[self.posy] += "#"
        else:
            self.image[self.posy] += "."

    def noop(self):
        self.drawSprite()

    def addx(self, arg):
        self.drawSprite()
        self.spritex += arg
        self.drawSprite()

    def printScreen(self):
        for h in range(self.height):
            print(self.image[h])


def part_2(input_data: list):
    """Solution code for Part 2. Should return the solution."""
    crt = CRT(40, 6)

    for op, arg in input_data:
        match op:
            case "noop":
                crt.noop()
            case "addx":
                crt.addx(arg)

    crt.printScreen()

    pass


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
