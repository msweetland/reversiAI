import unittest
import client
import utilities
import heuristics


class TestValidCoord(unittest.TestCase):
  def test_valid_coord(self):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    self.assertEqual(utilities.validCoord((0, 0), board), True)
    self.assertEqual(utilities.validCoord((-1, 0), board), False)
    self.assertEqual(utilities.validCoord((7, 7), board), True)


class TestGetOpponent(unittest.TestCase):
  def test_get_opponent(self):
    self.assertEqual(utilities.getOpponent(1), 2)
    self.assertEqual(utilities.getOpponent(2), 1)


class TestIsValidMove(unittest.TestCase):
  def test_is_valid_move(self):
    board1 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0, 0, 0],
        [0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    self.assertEqual(utilities.isValidMove(
        (4, 2), 1, board1), [(4, 3), (4, 2)])
    self.assertEqual(utilities.isValidMove(
        (5, 3), 1, board1), [(4, 3), (5, 3)])
    self.assertEqual(utilities.isValidMove((0, 0), 1, board1), False)
    self.assertEqual(utilities.isValidMove((-1, -1), 1, board1), False)
    
    board2 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 2, 2, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    self.assertEqual(utilities.isValidMove(
        (2, 1), 1, board2), [(3, 2), (2, 1)])

    board3 = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 1, 0],
        [0, 1, 0, 0, 2, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    self.assertEqual(utilities.isValidMove(
        (1, 4), 1, board3), [(1, 5), (3, 4), (2, 4), (1, 4)])


class TestPlacement(unittest.TestCase):
  def test_placement(self):
    boardbefore = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 1, 0],
        [0, 1, 0, 0, 2, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    boardafter = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 2, 2, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    player = 1
    validMoves = utilities.isValidMove((1, 4), player, boardbefore)
    for c in validMoves:
      utilities.setTile(c, player,  boardbefore)
    self.assertEqual(boardbefore, boardafter)


class TestScore(unittest.TestCase):
  def test_score(self):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 2, 2, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    self.assertEqual(utilities.scoreBoard(board), (9, 7))


class TestHeuristicScoreDiff(unittest.TestCase):
  def test_score(self):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 2, 2, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    self.assertEqual(heuristics.scoreDiff(board, 1), 2)



if __name__ == '__main__':
  unittest.main()
