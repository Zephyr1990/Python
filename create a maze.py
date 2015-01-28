import random

CELLS = []

maze_size = int(input('What is the size of the maze? '))

for x in range(maze_size+1):
    for y in range(maze_size+1):
        tuple = (x, y)
        CELLS.append(tuple)
CELLS.sort()
print(CELLS)
