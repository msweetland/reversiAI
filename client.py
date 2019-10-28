#!/usr/bin/python

import sys
import json
import socket
import minimax


def get_move(player, board, turn):
  print("\nMaking choice")
  print ('Turn:', turn)
  choice = minimax.makeChoice(player, board)
  return choice

def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}\n'.format(response))
  return response

if __name__ == "__main__":
  turn = 0
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()
  print ('Client running on port:', port)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      print (json_data)
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print (player, maxTurnTime, board)
      move = get_move(int(player), board, turn)
      turn += 1
      response = prepare_response(list(move))
      sock.sendall(response)
  finally:
    sock.close()
