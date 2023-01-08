import typing

'''
Below is the standard object is_move_safe
is_move_safe = {
  "up": True, 
  "down": True, 
  "left": True, 
  "right": True
}
The following is passed from main, extracted from the game_state object.
board: https://docs.battlesnake.com/api/objects/board
you: https://docs.battlesnake.com/api/objects/battlesnake
'''

def avoid_moving_backwards(
  board: typing.Dict, 
  you: typing.Dict,
  is_move_safe: typing.Dict
) -> typing.Dict:

  # We've included code to prevent your Battlesnake from moving backwards
  my_head = you["body"][0]  # Coordinates of your head
  my_neck = you["body"][1]  # Coordinates of your "neck"

  print("Position: ", "head -", my_head, "neck -", my_neck)

  if my_neck["x"] < my_head["x"]:  
    # Neck is left of head, don't move left
    is_move_safe["left"] = False
    
  elif my_neck["x"] > my_head["x"]:  
    # Neck is right of head, don't move right
    is_move_safe["right"] = False

  elif my_neck["y"] < my_head["y"]:  
    # Neck is below head, don't move down
    is_move_safe["down"] = False

  elif my_neck["y"] > my_head["y"]:  
    # Neck is above head, don't move up
    is_move_safe["up"] = False
  
  return is_move_safe

def avoid_walls(
  board: typing.Dict, 
  you: typing.Dict,
  is_move_safe: typing.Dict
) -> typing.Dict:
  # TODO: Step 1 - Prevent your Battlesnake from moving out of bounds

  board_width = board['width']
  board_height = board['height']

  my_head = you["body"][0]  # Coordinates of your head

  if my_head["x"] == board_width - 1:
    is_move_safe["right"] = False
  
  if my_head["x"] == 0:
    is_move_safe["left"] = False

  if my_head["y"] == board_height - 1:
    is_move_safe["up"] = False

  if my_head["y"] == 0:
    is_move_safe["down"] = False

  return is_move_safe

def avoid_yourself(
  board: typing.Dict, 
  you: typing.Dict,
  is_move_safe: typing.Dict
) -> typing.Dict:
  # TODO: Step 2 - Prevent your Battlesnake from colliding with     itself
  # my_body = game_state['you']['body']
  return is_move_safe

def avoid_other_snakes(
  board: typing.Dict, 
  you: typing.Dict,
  is_move_safe: typing.Dict
) -> typing.Dict:
    # TODO: Step 3 - Prevent your Battlesnake from colliding with other Battlesnakes
  # opponents = game_state['board']['snakes']
  return is_move_safe