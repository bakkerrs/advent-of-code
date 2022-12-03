def input():
    with open("./2022/day 02/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# The mapping from letters to shapes
shapes = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "rock",
  "Y": "paper",
  "Z": "scissors"
}

# The mapping from letters to scores
scores = {
  "A": 1,
  "B": 2,
  "C": 3,
  "X": 1,
  "Y": 2,
  "Z": 3
}

# The total score
total_score = 0

# Read the input
for line in input():
  try:
    # Read the opponent's move and your response
    opponent, response = line.split()

    # Get the shapes for the opponent's move and your response
    opponent_shape = shapes[opponent]
    response_shape = shapes[response]

    # Calculate the score for the round
    if opponent_shape == response_shape:
      # It's a draw
      score = 3
    elif (opponent_shape == "rock" and response_shape == "paper") or \
         (opponent_shape == "paper" and response_shape == "scissors") or \
         (opponent_shape == "scissors" and response_shape == "rock"):
      # You win
      score = 6
    else:
      # You lose
      score = 0

    # Add the score for your move to the total score
    total_score += scores[response] + score
  except EOFError:
    # End of input, stop reading
    break

# Print the result
print("Your total score would be", total_score)