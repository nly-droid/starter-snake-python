# Welcome to
# __________         __    __  .__                               __
# \______   \_____ _/  |__/  |_|  |   ____   ______ ____ _____  |  | __ ____
#  |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___//    \\__  \ |  |/ // __ \
#  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   |  \/ __ \|    <\  ___/
#  |________/(______/__|  |__| |____/\_____>______>___|__(______/__|__\\_____>
#
# This file can be a nice home for your Battlesnake logic and helper functions.
#
# To get you started we've included code to prevent your Battlesnake from moving backwards.
# For more info see docs.battlesnake.com

import random
import typing
from compile_safe_moves import avoid_moving_backwards, avoid_walls, avoid_yourself, avoid_other_snakes

# info is called when you create your Battlesnake on play.battlesnake.com
# and controls your Battlesnake's appearance
# TIP: If you open your Battlesnake URL in a browser you should see this data
def info() -> typing.Dict:
  print("INFO")

  return {
      "apiversion": "1",
      "author": "",  # TODO: Your Battlesnake Username
      "color": "#00cccc",  # TODO: Choose color
      "head": "do-sammy",  # TODO: Choose head
      "tail": "do-sammy",  # TODO: Choose tail
  }


# start is called when your Battlesnake begins a game
def start(game_state: typing.Dict):
  print("GAME START")


# end is called when your Battlesnake finishes a game
def end(game_state: typing.Dict):
  print("GAME OVER\n")


# move is called on every turn and returns your next move
# Valid moves are "up", "down", "left", or "right"
# See https://docs.battlesnake.com/api/example-move for available data
def move(game_state: typing.Dict) -> typing.Dict:

  is_move_safe = {
    "up": True, 
    "down": True, 
    "left": True, 
    "right": True
  }

  board = game_state['board']
  you = game_state['you']

  is_move_safe = avoid_moving_backwards(board, you, is_move_safe)
  is_move_safe = avoid_walls(board, you, is_move_safe)
  is_move_safe = avoid_yourself(board, you, is_move_safe)
  is_move_safe = avoid_other_snakes(board, you, is_move_safe)
  
  # Are there any safe moves left?
  safe_moves = []
  for move, isSafe in is_move_safe.items():
      if isSafe:
          safe_moves.append(move)

  if len(safe_moves) == 0:
      print(f"MOVE {game_state['turn']}: No safe moves detected! Moving down")
      return {"move": "down"}

  # Choose a random move from the safe ones
  next_move = random.choice(safe_moves)

  # TODO: Compile optimal moves from the list of safe moves

  print(f"MOVE {game_state['turn']}: {next_move}")
  return {"move": next_move}


# Start server when `python main.py` is run
if __name__ == "__main__":
  from server import run_server

  run_server({
      "info": info, 
      "start": start, 
       "move": move, 
      "end": end
  })
