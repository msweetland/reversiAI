import utilities

def scoreDiff(board, currentplayer):
  (p1, p2) = utilities.scoreBoard(board)
  if currentplayer == 1:
    return p1 - p2
  else:
    return p2 - p1
