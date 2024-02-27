from itertools import cycle

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def part1():
    f = open("input.txt")
    directions = cycle(f.readline().strip())
    f.readline()
    tree = {}
    for line in f:
        line = line.split('=')
        key = line[0].strip()
        line = line[1].split(',')
        tree[key] = Node(line[0].strip("() \n"), line[1].strip("\n() "))
    
    steps = 0
    currentNode = "AAA"

    
    for d in directions:
        if d == 'L':
            currentNode = tree[currentNode].left
        else:
            currentNode = tree[currentNode].right
        
        steps += 1
        if currentNode == "ZZZ":
            break

    print(steps)

def step(currentNode, tree, d):
    if d == 'L':
        currentNode = tree[currentNode].left
    else:
        currentNode = tree[currentNode].right
    return currentNode

def reachedDestination(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True

def gcd(x, y):
    while 0 != y and x != 0:
        if x < y:
            x, y = y, x
        x, y = x % y, y
    
    return y

def lcm(x, y):
    return x * y / gcd(x, y)

def part2():
    startNodes = []
    f = open("input.txt")
    directions = cycle(f.readline().strip())
    f.readline()
    tree = {}
    for line in f:
        line = line.split('=')
        key = line[0].strip()
        if key[-1] == 'A':
            startNodes.append(key)
        line = line[1].split(',')
        tree[key] = Node(line[0].strip("() \n"), line[1].strip("\n() "))
    
    steps = 0
    stepsRequired = []

    for node in startNodes:
        steps = 0
        for d in directions:
            node = step(node, tree, d)
            steps += 1
            if node[-1] == 'Z':
                break
        stepsRequired.append(steps)

    sol = 1

    for s in stepsRequired:
        sol = lcm(sol, s)
    
    print(sol)

part2()