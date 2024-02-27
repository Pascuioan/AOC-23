import copy
import math
import heapq
from threading import Thread

def search(start, end, map, visited):
    steps = 0

    while True:
        if start == end:
            return steps
        visited[start[0]][start[1]] = True
        options = []
        # left
        next = (start[0], max(0, start[1] - 1))
        if not visited[next[0]][next[1]] and (map[next[0]][next[1]] in ".v^<"):
            options.append(next)
        # right
        next = (start[0], min(len(map[0]) - 1, start[1] + 1))
        if not visited[next[0]][next[1]] and (map[next[0]][next[1]] in ".v^>"):
            options.append(next)
        # up
        next = (max(0, start[0] - 1), start[1])
        if not visited[next[0]][next[1]] and (map[next[0]][next[1]] in ".<^>"):
            options.append(next)
        # down
        next = (min(len(map) - 1, start[0] + 1), start[1])
        if not visited[next[0]][next[1]] and (map[next[0]][next[1]] in ".v<>"):
            options.append(next)
        
        if options == []:
            return -1

        if len(options) == 1:
            start = options[0]
            steps += 1
        else:
            break
    
    m = [search(next, end, map, copy.deepcopy(visited)) for next in options]

    return 1 + steps + max(*m)

def part1():
    map = []
    for line in open("input.txt"):
        map.append(line.strip())
    start = (0, map[0].index('.'))
    end = (len(map) - 1, map[-1].index('.'))

    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]

    print(search(start, end, map, visited))

def getOptions(node, map):
    options = []
    x, y = node[0], node[1]
    height, width = len(map), len(map[0])

    if x - 1 >= 0:
        if map[x - 1][y] == '.':
            options.append((x - 1, y))
    if x + 1 < height:
        if map[x + 1][y] == '.':
            options.append((x + 1, y))
    if y - 1 >= 0:
        if map[x][y - 1] == '.':
            options.append((x, y - 1))
    if y + 1 < width:
        if map[x][y + 1] == '.':
            options.append((x, y + 1))
    
    return options

def getNodes(start, end, map):
    nodes = [start, end]
    toVisit = [start]
    visited = [[False for _ in range(len(map[0]))] for _ in range(len(map))]
    while toVisit != []:
        start = toVisit.pop(0)
        while True:
            visited[start[0]][start[1]] = True
            options = []
            # left
            next = (start[0], max(0, start[1] - 1))
            if not visited[next[0]][next[1]] and (map[next[0]][next[1]] == '.'):
                options.append(next)
            # right
            next = (start[0], min(len(map[0]) - 1, start[1] + 1))
            if not visited[next[0]][next[1]] and (map[next[0]][next[1]] == '.'):
                options.append(next)
            # up
            next = (max(0, start[0] - 1), start[1])
            if not visited[next[0]][next[1]] and (map[next[0]][next[1]] == '.'):
                options.append(next)
            # down
            next = (min(len(map) - 1, start[0] + 1), start[1])
            if not visited[next[0]][next[1]] and (map[next[0]][next[1]] == '.'):
                options.append(next)

            if len(options) == 0:
                break
            if len(options) > 1:
                nodes.append(start)
                toVisit.extend(options)
                break
            start = options[0]

    return list(set(nodes))

def buildEdges(nodes, map):
    edges = {}
    for node in nodes:
        edges[node] = set()

    for node in nodes:

        options = getOptions(node, map)
        for option in options:
            previous = node
            next = option
            steps = 1
            while True:
                if next in nodes:
                    break
                steps += 1
                op = getOptions(next, map)
                if op[0] != previous:
                    previous, next = next, op[0]
                else:
                    previous, next = next, op[1]

            edges[next].add((steps, node))
            edges[node].add((steps, next))
    
    return edges

def dfs(start, end, edges, visited, result):
    # if start == end:
    #     return 0
    
    # visited[start] = True

    # m = 0
    
    # for cost, next in edges[start]:
    #     if not visited[next]:
    #         m = max(m, cost + dfs(next, end, edges, copy.deepcopy(visited), []))

    # return m
    print("t",end="")
    if start == end:
        return
        result[0] = 0

    visited[start] = True

    threads = []
    results = []

    for cost, next in edges[start]:
        if not visited[next]:
            results.append([cost])
            threads.append(Thread(target=dfs, args = (next, end, edges, copy.deepcopy(visited), results[-1])))
            # dfs(next, end, edges, copy.deepcopy(visited), newRes)
            # result[0] = max(result[0], cost + newRes[0])

    if threads == []:
        return

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    results = [r[0] for r in results]

    result[0] += max(results)


def part2():
    map = []
    for line in open("input.txt"):
        map.append(line.strip())

    map = [row.replace("<", ".").replace(">", ".").replace("v", ".").replace("^", ".") for row in map]

    start = (0, map[0].index('.'))
    end = (len(map) - 1, map[-1].index('.'))

    nodes = getNodes(start, end, map)
    edges = buildEdges(nodes, map)
    visited = {node : False for node in nodes}

    res = [0]
    dfs(start, end, edges, visited, res)
    print("\n", res[0])

part2()

#####.######################
#...................########
#.###.#########.###.########
#.......................####
#####.#########.###.###.####
#####.#########.###.###.####
#####...............###.####
#######################.####
#######################.####
#######################.####
#######################.####