# Advent of Code 2022
# Day 07
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

    fs = {"/": {"type": "dir", "size": 0}}
    current_dir = []
    current_path = "/"

    def addsize(size):
        nonlocal current_dir
        nonlocal current_path
        nonlocal fs
        fs["/"]["size"] += size
        if current_dir != []:
            path = "/"
            for dir in current_dir:
                path += dir + "/"
                fs[path]["size"] += size

    def ls():
        nonlocal current_dir
        nonlocal current_path
        nonlocal fs
        while True:
            line = raw_input.readline().rstrip()
            if line == "":
                break
            if line[0] == "$":
                indicator, command, params = line.split(" ")
                change_directory(params)
                break

            filetype, filename = line.split(" ")
            path = current_path + filename

            if filetype == "dir":
                fs[path + "/"] = {"type": "dir", "size": 0}
            else:
                fs[path] = {"type": "file", "size": int(filetype)}
                addsize(int(filetype))
        pass

    def change_directory(destination):
        nonlocal current_dir
        nonlocal current_path
        nonlocal fs
        if destination == "..":
            current_dir.pop()
            path = "/"
            for dir in current_dir:
                path += dir + "/"
            current_path = path
        elif destination == "/":
            current_path = "/"
            current_dir = []
        else:
            current_dir.append(destination)
            path = "/"
            for dir in current_dir:
                path += dir + "/"
            current_path = path
        pass

    with open(data_path, "r") as raw_input:

        while True:
            line = raw_input.readline().rstrip()
            if line == "":
                break
            line = line.split(" ")
            indicator = line[0]
            if indicator != "$":
                print("parsing error")
                break
            match line[1]:
                case "cd":
                    change_directory(line[2])
                case "ls":
                    ls()

        return fs


def part_1(input_data: list):
    """Solution code for Part 1. Should return the solution."""
    total = 0
    for path in input_data:
        data = input_data[path]
        if data["type"] == "dir" and data["size"] <= 100000:
            total += data["size"]

    return total


def part_2(input_data: list):
    """Solution code for Part 2. Should return the solution."""
    space_required = 30000000 - (70000000 - input_data["/"]["size"])
    min_space = 70000000
    for path in input_data:
        data = input_data[path]
        if (
            data["type"] == "dir"
            and data["size"] >= space_required
            and data["size"] < min_space
        ):
            min_space = data["size"]

    return min_space


def run_direct():
    """
    This function runs if this file is executed directly, rather than using the
    justfile interface. Useful for quick debugging and checking your work.
    """
    input = parse_input(SAMPLE_PATH)
    print(input)
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
