import math
import copy
import utilities
import heuristics

def minimax(board, originalPlayer: int, currentplayer: int, depth: int,) -> float:
  """Minimax algorithm"""
  if depth == 0:
    return heuristics.scoreDiff(board, currentplayer)

  possibleMoves = utilities.getValidMoves(currentplayer, board)
  scores = []
  for move in possibleMoves:
    coord, validMoves = move
    tempBoard = copy.deepcopy(board)
    opponent = utilities.getOpponent(currentplayer)
    heuristic = minimax(tempBoard, originalPlayer, opponent, depth - 1)
    scores.append(heuristic)

  isMaximizing = originalPlayer == currentplayer

  if isMaximizing:
    if len(scores) == 0:
      return -math.inf
    return max(scores)
  else:
    if len(scores) == 0:
      return math.inf
    return min(scores)


def makeChoice(player, board):
  possibleMoves = utilities.getValidMoves(player, board)
  ranked = []
  for move in possibleMoves:
    coord, tiles = move
    tempBoard = copy.deepcopy(board)

    for m in tiles:
      utilities.setTile(m, player,  tempBoard)

    opponent = utilities.getOpponent(player)
    heuristic = minimax(tempBoard, player, opponent, 3)
    ranked.append((coord, heuristic))

  return max(ranked, key=lambda r: r[1])[0]
