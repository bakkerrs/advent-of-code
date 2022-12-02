def get_input():
    with open("./2020/1/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# Part 1: What would your total score be if everything goes exactly according to your strategy guide?
def part1(input): 
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

    for round in input:
        opponent, you = round.split(" ")
        opponent = shapes[opponent]
        you = shapes[you]
        score += shapeScore[you] + result[you][opponent]

    return score
        
# Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def part2(input):
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
    for round in input:
        opponent, outcome = round.split(" ")
        opponent = shapes[opponent]
        outcome = outcomes[outcome]
        score += playedShape[opponent][outcome] + outcome

    return score

def main():
    print(part1(get_input()))
    print(part2(get_input()))



    pass

main()