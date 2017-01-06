import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

x = 5
y = 1

myID, game_map = hlt.get_init()
hlt.send_init("YourPythonBot")

def assign_move(square):
    secure = True
    insecure = True
    bolster, direct = (0, STILL)
    rally, director = (255, STILL)
    avail = [direction for direction, neighbor in enumerate(game_map.neighbors(square)) if neighbor.owner == myID]

    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner != myID:
            secure = False
            if neighbor.strength < square.strength:
                return Move(square, direction)
        else:
            insecure = False
            if neighbor.strength > bolster:
                bolster, direct = (neighbor.strength, direction)
            if neighbor.strength > y * neighbor.production:
                if neighbor.strength < rally:
                    rally, director = (neighbor.strength, direction)

    if square.strength < x * square.production:
        return Move(square, STILL)
    elif secure:
        if bolster > 1.5 * square.strength:
            return Move(square, direct)
        elif rally < 255:
            return Move(square, director)
        else:
            return Move(square, random.choice((NORTH,EAST)))
    elif insecure:
        return Move(square, STILL)
    else:
        return Move(square, expand(avail, square.x, square.y))
        
def expand(avail, x, y):
    if len(avail) == 1:
        return avail[0]

    xs = [a for a in avail if (a == EAST  or a == WEST) ]
    ys = [a for a in avail if (a == NORTH or a == SOUTH)]

    if len(xs) == 2:
        dx = EAST
    else:
        if EAST in xs:
            dx = EAST
        elif WEST in xs:
            dx = WEST
        else:
            dx = STILL
    if len(ys) == 2:
        dy = NORTH
    else:
        if NORTH in ys:
            dy = NORTH
        elif SOUTH in ys:
            dy = SOUTH
        else:
            dy = STILL
    if dx == STILL:
        return dy
    elif dy == STILL:
        return dx
    else:
        return random.choice((dx,dy))

while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
