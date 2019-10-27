
# ex
# [
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,2,0,0,0],
#   [0,0,0,0,2,0,0,0],
#   [0,0,0,1,2,0,0,0],
#   [0,0,0,1,2,2,0,0],
#   [0,0,0,1,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0]
# ]


def isValidMove(coord, player, board):

  opponent = 1 if player == 1 else 2

  pass


H = len(board)
W = len(board[0])


def validCoord(coord):
    r, c = coord
    return r >= 0 and r < H and c >= 0 and c < W

# col == 0:
# topLeft = validOthello((rI - 1, cI - 1))
# top = validOthello((rI - 1, cI))
# topRight = validOthello((rI - 1, cI + 1))
# bottomLeft = validOthello((rI + 1, cI - 1))
# bottom = validOthello((rI + 1, cI))
# bottomRight = validOthello((rI + 1, cI + 1))
# left = validOthello((rI, cI - 1))
# right = validOthello((rI, cI + 1))
# if (topLeft or top or topRight or bottomLeft or bottom or bottomRight or left or right):
#   valids.append((rI, cI))

def valid_moves(player, board):
  """Returns array of tupples of vlaid coordinates"""
  """Player = 1 or 2"""

  valids = []

  for rI, row in enumerate(board):
    for cI, col in enumerate(row):
      if isValidMove((rI, cI), player, board):
        valids.append((rI, cI))
  
  return valids




def isCorner(coord, board):
  """Returns bool if coord is corner."""
  H = len(board)
  W = len(board[0])

  rI, cI = coord
  return (
    (rI == 0 and cI == 0) or
    (rI == 0 and cI == W - 1) or
    (rI == H - 1 and cI == 0) or
    (rI == H - 1 and cI == W - 1)
  )
    
