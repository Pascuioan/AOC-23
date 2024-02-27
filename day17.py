from queue import PriorityQueue
import math
inf = math.inf

def minus(pair1, pair2):
    return(pair1[0] - pair2[0], pair1[1] - pair2[1])

def canContinue(coord, parents):
    steps = []
    while (coord != (-1,-1)) and (len(steps) != 4):
        steps.append(coord)
        coord = parents[coord[0]][coord[1]]

    if len(steps) != 4:
        return True
    
    steps = [minus(steps[i], steps[i + 1]) for i in range(3)]

    if steps[0] == steps[1] == steps[2]:
        return False
    return True

def neighbours(coord, height, width):
    s = set()
    s.add((max(coord[0] - 1, 0), coord[1]))
    s.add((min(coord[0] + 1, height - 1), coord[1]))
    s.add((coord[0], max(coord[1] - 1, 0)))
    s.add((coord[0], min(coord[1] + 1, width - 1)))
    s.discard(coord)
    return list(s)


def part1():
    blocks = []
    for line in open("input.txt"):
        blocks.append([int(x) for x in line.strip()])

    height, width = len(blocks), len(blocks[0])

    minCostToConnect = [[inf for _ in range(width)] for _ in range(height)]

    parents = [[-1 for _ in range(width)] for _ in range(height)]

    q = PriorityQueue()

    current = (0,0)
    minCostToConnect[0][0] = 0
    parents[0][0] = (-1,-1)
    q.put((0,(0,0)))
    end = (height - 1, width - 1)

    while current != end:
        current = q.get()
        current = current[1]

        next = neighbours(current, height, width)

        # if current == (0,3):
        #     pass

        # if not canContinue(current, parents):
        #     step = minus(current, parents[current[0]][current[1]])
        #     nextCoord = minus(current, (-step[0], -step[1]))
        #     if nextCoord in next:
        #         next.remove(nextCoord)

        for neighbour in next:
            if minCostToConnect[neighbour[0]][neighbour[1]] > (minCostToConnect[current[0]][current[1]] + blocks[neighbour[0]][neighbour[1]]):
                minCostToConnect[neighbour[0]][neighbour[1]] = minCostToConnect[current[0]][current[1]] + blocks[neighbour[0]][neighbour[1]]
                parents[neighbour[0]][neighbour[1]] = current
                q.put((blocks[neighbour[0]][neighbour[1]], neighbour))
        current = current

    path = [[0 for _ in range(width)] for _ in range(height)]

    while end != (0,0):
        path[end[0]][end[1]] = 1
        end = parents[end[0]][end[1]]

    print(*minCostToConnect, sep = '\n')

part1()    