import copy

def emptyUnder(brick, occupied):
    x1, x2 = brick[0][0], brick[1][0]
    y1, y2 = brick[0][1], brick[1][1]
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            under = occupied[brick[0][2] - 1][i][j]
            if under:
                return False
    return True

def getSupports(brick, occupied):
    supports = set()
    x1, x2 = brick[0][0], brick[1][0]
    y1, y2 = brick[0][1], brick[1][1]
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            under = occupied[brick[0][2] - 1][i][j]
            if (under != -1) and under:
                supports.add(under)
    return supports

def part1():
    bricks = []
    maxZ = 0
    for line in open("input.txt"):
        coord1, coord2 = line.strip().split("~")
        coord1, coord2 = coord1.split(","), coord2.split(",")
        coord1 = [int(x) for x in coord1]
        coord2 = [int(x) for x in coord2]
        maxZ = max(maxZ, max(coord1[2], coord2[2]))
        bricks.append((tuple(coord1), tuple(coord2)))
    bricks.sort(key = lambda x : x[0][2])
    occupied = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(maxZ + 1)]

    for i in range(10):
        for j in range(10):
            occupied[0][i][j] = -1

    supports = {}
    supported = {}
    
    for index, brick in enumerate(bricks):
        x1, x2 = brick[0][0], brick[1][0]
        y1, y2 = brick[0][1], brick[1][1]
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        # let the brick fall as much as it can
        while emptyUnder(brick, occupied):
            brick = ((x1, y1, brick[0][2] - 1), (x2, y2, brick[1][2] - 1))
        
        bricks[index] = brick
        supports[index + 1] = set()

        supps = getSupports(brick, occupied)
        supported[index + 1] = supps
        for b in supps:
            supports[b].add(index + 1)
                

        # fill in the brick
        for k in range(brick[0][2], brick[1][2] + 1):
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    occupied[k][i][j] = index + 1

    sol = 0
    for ind in range(1, len(bricks) + 1):
        for above in supports[ind]:
            if len(supported[above]) == 1:
                break
        else:
            sol += 1
    
    print(sol)

def bfs(start, supports, innerDegree):
    visited = [False for _ in range(len(supports) + 2)]
    innerDegree[start] = 0
    # visited[start] = True
    sum = 0
    changed = True
    while changed:
        changed = False
        for node, degree in enumerate(innerDegree):
            if (degree == 0) and (not visited[node]):
                sum += 1
                visited[node] = True
                for next in supports[node]:
                    innerDegree[next] -= 1
                changed = True
    
    return sum - 1


def part2():
    bricks = []
    maxZ = 0
    for line in open("input.txt"):
        coord1, coord2 = line.strip().split("~")
        coord1, coord2 = coord1.split(","), coord2.split(",")
        coord1 = [int(x) for x in coord1]
        coord2 = [int(x) for x in coord2]
        maxZ = max(maxZ, max(coord1[2], coord2[2]))
        bricks.append((tuple(coord1), tuple(coord2)))
    bricks.sort(key = lambda x : x[0][2])
    occupied = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(maxZ + 1)]

    for i in range(10):
        for j in range(10):
            occupied[0][i][j] = -1

    supports = {}
    supported = {}
    
    for index, brick in enumerate(bricks):
        x1, x2 = brick[0][0], brick[1][0]
        y1, y2 = brick[0][1], brick[1][1]
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        # let the brick fall as much as it can
        while emptyUnder(brick, occupied):
            brick = ((x1, y1, brick[0][2] - 1), (x2, y2, brick[1][2] - 1))
        
        bricks[index] = brick
        supports[index + 1] = set()

        supps = getSupports(brick, occupied)
        supported[index + 1] = supps
        for b in supps:
            supports[b].add(index + 1)

        # fill in the brick
        for k in range(brick[0][2], brick[1][2] + 1):
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    occupied[k][i][j] = index + 1

        supported[0] = set()
        supports[0] = set()

    innerDegree = [len(supported[x]) for x in range(len(bricks) + 1)]
    innerDegree[0] = 1
    for ind, brick in enumerate(bricks):
        if brick[0][2] == 1:
            innerDegree[ind + 1] = 1
    
    sol = [bfs(x, supports, copy.deepcopy(innerDegree)) for x in range(1, len(bricks) + 1)]
    
    print(sum(sol))


import time
start_time = time.time()
part2()
print("--- %s seconds ---" % (time.time() - start_time))