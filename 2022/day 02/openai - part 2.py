def input():
    with open("./2022/day 02/input.txt") as f:
        return [x.strip() for x in f.read().split("\n")]

# The mapping from letters to shapes
shapes = {
  "A": "rock",
  "B": "paper",
  "C": "scissors"
}

# The mapping from letters to scores
scores = {
  "A": 1,
  "B": 2,
  "C": 3,
  "rock": 1,
  "paper": 2,
  "scissors": 3
}

# The total score
total_score = 0

# Read the input
for line in input():
  try:
    # Read the opponent's move and the desired outcome
    opponent, outcome = line.split()

    # Get the shape for the opponent's move
    opponent_shape = shapes[opponent]

    # Calculate the shape to choose to achieve the desired outcome
    if outcome == "X":
      # You need to lose, choose the shape that loses to the opponent's shape
      if opponent_shape == "rock":
        response_shape = "scissors"
      elif opponent_shape == "paper":
        response_shape = "rock"
      else:
        response_shape = "paper"
    elif outcome == "Y":
      # You need to end in a draw, choose the same shape as the opponent
      response_shape = opponent_shape
    else:
      # You need to win, choose the shape that wins against the opponent's shape
      if opponent_shape == "rock":
        response_shape = "paper"
      elif opponent_shape == "paper":
        response_shape = "scissors"
      else:
        response_shape = "rock"

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
    total_score += scores[response_shape] + score
  except EOFError:
    # End of input, stop reading
    break

# Print the result
print("Your total score would be", total_score)
