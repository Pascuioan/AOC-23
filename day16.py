from enum import Enum
import time
class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1,0)
    RIGHT = (0,1)
    LEFT = (0,-1)

def inBounds(coords, matrix):
    height = len(matrix)
    width = len(matrix[0])
    if 0 <= coords[0] < height and 0 <= coords[1] < width:
        return True
    return False

def step(coords, direction):
    return (coords[0] + direction.value[0], coords[1] + direction.value[1])

def shine(coords, direction, matrix, energized, hasBennSplit):
    while inBounds(coords, matrix):
        i, j = coords[0], coords[1]
        energized[i][j] = 1
        match matrix[i][j]:
            case '|':
                if direction.value[0] == 0:
                    if hasBennSplit[i][j] == 0:
                        hasBennSplit[i][j] = 1
                        shine(step(coords, Direction.UP), Direction.UP, matrix, energized, hasBennSplit)
                        shine(step(coords, Direction.DOWN), Direction.DOWN, matrix, energized, hasBennSplit)
                    return
            case '-':
                if direction.value[1] == 0:
                    if hasBennSplit[i][j] == 0:
                        hasBennSplit[i][j] = 1
                        shine(step(coords, Direction.RIGHT), Direction.RIGHT, matrix, energized, hasBennSplit)
                        shine(step(coords, Direction.LEFT), Direction.LEFT, matrix, energized, hasBennSplit)
                    return
            case '/':
                match direction:
                    case Direction.UP:
                        direction = Direction.RIGHT
                    case Direction.DOWN:
                        direction = Direction.LEFT
                    case Direction.LEFT:
                        direction = Direction.DOWN
                    case Direction.RIGHT:
                        direction = Direction.UP
            case '\\':
                match direction:
                    case Direction.UP:
                        direction = Direction.LEFT
                    case Direction.DOWN:
                        direction = Direction.RIGHT
                    case Direction.LEFT:
                        direction = Direction.UP
                    case Direction.RIGHT:
                        direction = Direction.DOWN
        coords = (coords[0] + direction.value[0], coords[1] + direction.value[1])
                    


def part1(coords, direction):
    matrix = []
    for line in open("input.txt"):
        matrix.append(line.strip())
    energized = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    hasBennSplit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    shine(coords, direction, matrix, energized, hasBennSplit)

    return sum([sum(row) for row in energized])



def part2():
    matrix = []
    height = 0
    for line in open("input.txt"):
        height += 1
        matrix.append(line.strip())
        
    width = len(matrix[0])
    
    maximum = 0

    for i in range(height):
        energized = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        hasBennSplit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        shine((i,0), Direction.RIGHT, matrix, energized, hasBennSplit)
        maximum = max(maximum, sum([sum(row) for row in energized]))

        energized = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        hasBennSplit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        shine((i,width - 1), Direction.LEFT, matrix, energized, hasBennSplit)
        maximum = max(maximum, sum([sum(row) for row in energized]))
    for i in range(width):
        energized = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        hasBennSplit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        shine((0,i), Direction.DOWN, matrix, energized, hasBennSplit)
        maximum = max(maximum, sum([sum(row) for row in energized]))

        energized = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        hasBennSplit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        shine((height - 1,i), Direction.UP, matrix, energized, hasBennSplit)
        maximum = max(maximum, sum([sum(row) for row in energized]))

    print(maximum)

t = time.clock()

# part1((0,0), Direction.RIGHT)
part2()

print("--- %s seconds ---" % (time.time() - t))