import random

CELLS = []

maze_size = int(input('What is the size of the maze? '))

for x in range(maze_size+1):
    for y in range(maze_size+1):
        tuple = (x, y)
        CELLS.append(tuple)
CELLS.sort()

def get_locations():
  monster = random.choice(CELLS)
  door = random.choice(CELLS)
  start = random.choice(CELLS)
  
  if monster == door or monster == start or door == start:
    return get_locations
  
  return monster, door, start
  
  
def move_player(player, move):
  x, y = player
  
  if move == 'LEFT':
    y -= 1
  elif move == 'RIGHT':
    y += 1
  elif move ==  'UP':
    x -= 1
  elif move == 'DOWN':
    x += 1
  
  return x,y


def get_moves(player):
  moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # player = (x,y)
  if player[1] == 0:
    moves.remove('LEFT')
  if player[1] == 2:
    moves.remove('RIGHT')
  if player[0] == 0:
    moves.remove('UP')
  if player[0] == 2:
    moves.remove('DOWN')

  return moves

def draw_map(player):
  print(' _ _ _')
  tile = '|{}'
  
  for idx, cell in enumerate(CELLS):
    if idx in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print(tile.format('X'), end='')
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))
        
monster, door, player = get_locations()
print("Welcome to the dungeon!")
while True:
  moves = get_moves(player)
  
  print("You're currently in room {}".format(player))  # fill in with player position
  
  draw_map(player)
  
  
  print("You can move {}".format(moves))  # fill in with available moves
  print("Enter QUIT to quit")
  
  move = input("> ")
  move = move.upper()
  
  if move == 'QUIT':
    break
    
    
  if move in moves:
    player = move_player(player, move)
  else:
    print('Dont walk into walls!')
    continue
          
  if player == door:
    print("You escaped!")
    break
  elif player == monster:
    print("You lost!")
    break       
          
    
  # If it's a good move, change the player's position
  # If it's a bad move, don't change anything
  # If the new player position is the door, they win!
  # If the new player position is the monster, they lose!
  # Otherwise, continue
