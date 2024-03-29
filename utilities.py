def getOpponent(player):
  """Return oponnent number. Assumess player is 1 or 2"""
  assert player == 1 or player == 2, "Player must be 1 or 2"
  return 2 if player == 1 else 1


def validCoord(coord, board):
  """Checks if coord is within board indices."""
  assert len(coord) == 2
  r, c = coord
  H = len(board)
  W = len(board[0])
  return r >= 0 and r < H and c >= 0 and c < W


def isValidMove(coord, player, board):
  """Return array of coordinates to flip """
  """Inspired by https://inventwithpython.com/chapter15.html """
  assert len(coord) == 2
  r, c = coord
  if board[r][c] != 0 or not validCoord(coord, board):
    return False

  board[r][c] = player

  opponent = getOpponent(player)
  directions = [
    (-1, -1),   # top left
    (-1, 0),    # top
    (-1, 1),    # top right
    (0, -1),    # left
    (0, 1),     # right
    (1, -1),    # bootom left
    (1, 0),     # bottom
    (1, 1)      # bottom right
  ]

  tilesToClaim = []
  for (dR, dC) in directions:
    tR, tC = r + dR, c + dC
    if (
      validCoord((tR, tC), board) and
      board[tR][tC] == opponent
    ):
      tR, tC = tR + dR, tC + dC
      if not validCoord((tR, tC), board):
        continue
      while board[tR][tC] == opponent:
        tR, tC = tR + dR, tC + dC
        if not validCoord((tR, tC), board):
          break
      if not validCoord((tR, tC), board):
        continue
      if board[tR][tC] == player:
        while True:
          tR, tC = tR - dR, tC - dC
          if tR == r and tC == c:
            break
          tilesToClaim.append((tR, tC))
  board[r][c] = 0
  if len(tilesToClaim) == 0:
    return False

  tilesToClaim.append(coord)
  return tilesToClaim


def getValidMoves(player, board):
  """Returns array of tupples of valid coordinates"""
  valids = []
  for rI, row in enumerate(board):
    for cI, col in enumerate(row):
      tilesToChange = isValidMove((rI, cI), player, board)
      if tilesToChange:
        valids.append(((rI, cI), tilesToChange))
  return valids


def setTile(coord, player, board):
  """sets tile on board"""
  r, c = coord
  board[r][c] = player


def scoreBoard(board):
  """Return tuple: index 0 is player 1, index 1 is player 2"""
  p1Score = 0
  p2Score = 0
  for row in board:
    for col in row:
      if col == 1:
        p1Score += 1
      elif col == 2:
        p2Score += 1
  return (p1Score, p2Score)


def isGameOver(board):
  pass


if __name__ == "__main__":
  pass
