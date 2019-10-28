import math
import copy
import utilities
import heuristics


def minimax(board, originalPlayer, currentplayer, depth, alpha=-math.inf, beta=math.inf) -> float:
  """Minimax algorithm"""
  if depth == 0:
    return heuristics.mixed(board, currentplayer)

  possibleMoves = utilities.getValidMoves(currentplayer, board)
  isMaximizing = originalPlayer == currentplayer
  opponent = utilities.getOpponent(currentplayer)

  if isMaximizing:
    bestValue = -math.inf
    for move in possibleMoves:
      coord, tiles = move
      tempBoard = copy.deepcopy(board)
      for m in tiles:
        utilities.setTile(m, currentplayer,  tempBoard)

      heuristic = minimax(tempBoard, originalPlayer,
                          opponent, depth - 1, bestValue, beta)
      if heuristic > bestValue:
        bestValue = heuristic
      if bestValue > beta:
        return beta
    return bestValue
  else:
    bestValue = math.inf
    for move in possibleMoves:
      coord, tiles = move
      tempBoard = copy.deepcopy(board)
      for m in tiles:
        utilities.setTile(m, currentplayer,  tempBoard)

      heuristic = minimax(tempBoard, originalPlayer,
                          opponent, depth - 1, alpha, bestValue)
      if heuristic < bestValue:
        bestValue = heuristic
      if bestValue < alpha:
        return alpha
    return bestValue


def makeChoice(player, board):
  """minimax setup"""
  possibleMoves = utilities.getValidMoves(player, board)
  print (len(possibleMoves))
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
