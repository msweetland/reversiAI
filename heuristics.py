import utilities


def scoreDiff(board, currentplayer):
  """Normalized score between players"""
  (p1, p2) = utilities.scoreBoard(board)
  if currentplayer == 1:
    return p1 - p2 / (p2 + p1)
  else:
    return p2 - p1 / (p2 + p1)


def valueMatrix(board, currentPlayer):
  """Reward matrix"""
  V = [
    [300, -20, 20, 5, 5, 20, -20, 300],
    [-20, -60, -5, -5, -5, -5, -60, -20],
    [20, -5,  15,  3, 3, 15, -5, 20],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [20, -5,  15,  3, 3, 15, -5, 20],
    [-20, -60, -5, -5, -5, -5, -60, -20],
    [300, -20, 20, 5, 5, 20, -20, 300]
  ]

  # total = 376

  opponent = utilities.getOpponent(currentPlayer)
  s = 0

  for rI, row in enumerate(board):
    for cI, col in enumerate(row):
      if col == currentPlayer:
        s += V[rI][cI]
      elif col == opponent:
        s -= V[rI][cI]
  return s


def bigObreaker(board, currentPlayer):
  """Maximize runtime for opponent LOL"""
  possibleMoves = utilities.getValidMoves(currentPlayer, board)
  return len(possibleMoves) * -1


def mixed(board, currentPlayer):
  # a = scoreDiff(board, currentPlayer)
  # b = valueMatrix(board, currentPlayer)
  # c = bigObreaker(board, currentPlayer)
  # print(a, b)
  return valueMatrix(board, currentPlayer)


# V = [
#     [3.2125, 1.775, 1.875, 1.975, 1.975, 1.875, 1.775, 3.2125],
#     [0.1500, 2.3, 0.6625, 1.8375, 1.8375, 0.6625, 2.3, 0.1500],
#     [3.5250, 0.85, 2.675, 0.1750, 0.1750, 2.675, 0.85, 3.5250],
#     [1.125, 1.95, 0.15, 0.0, 0.0, 0.15, 1.95, 1.125],
#     [1.125, 1.95, 0.15, 0.0, 0.0, 0.15, 1.95, 1.125],
#     [3.5250, 0.85, 2.675, 0.1750, 0.1750, 2.675, 0.85, 3.5250],
#     [0.1500, 2.3, 0.6625, 1.8375, 1.8375, 0.6625, 2.3, 0.1500],
#     [3.2125, 1.775, 1.875, 1.975, 1.975, 1.875, 1.775, 3.2125],
# ]
