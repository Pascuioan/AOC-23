def convertDir(n):
    match(int(n)):
        case 0:
            return 'R'
        case 1:
            return 'D'
        case 2:
            return 'L'
        case 3:
            return 'U'

def getDir(c):
    match(c):
        case 'R':
            return (0, 1)
        case 'L':
            return (0, -1)
        case 'U':
            return (-1, 0)
        case 'D':
            return (1, 0)

def part1():
    size = 500
    ground = [['.' for _ in range(size)] for _ in range(size)]
    visited = [[False for _ in range(size)] for _ in range(size)]
    instructions = []
    for line in open("input.txt"):
        line = line.strip().split()
        direction, length, color = line[0], int(line[1]), line[2].strip("()")
        instructions.append((direction, length, color))
    
    location = (size // 2, size // 2)

    ground[location[0]][location[1]] = '#'
    for instruction in instructions:
        direction = getDir(instruction[0])
        steps = instruction[1]
        for _ in range(steps):
            location = (location[0] + direction[0], location[1] + direction[1])
            ground[location[0]][location[1]] = '#'
    
    q = []
    ground = [row for row in ground if '#' in row]

    height = len(ground) // 2
    for i in range(len(ground[0])):
        if ground[height][i] == '#':
            i += 1
            while ground[height][i] == '#':
                i += 1
            bfsLocation = (height, i)
            break
    
    q.append(bfsLocation)
    
    while q != []:
        bfsLocation = q.pop(0)
        ground[bfsLocation[0]][bfsLocation[1]] = '#'
        if (ground[bfsLocation[0] + 1][bfsLocation[1]] == '.') and (not visited[bfsLocation[0] + 1][bfsLocation[1]]):
            visited[bfsLocation[0] + 1][bfsLocation[1]] = True
            q.append((bfsLocation[0] + 1, bfsLocation[1]))

        if (ground[bfsLocation[0] - 1][bfsLocation[1]] == '.') and (not visited[bfsLocation[0] - 1][bfsLocation[1]]):
            visited[bfsLocation[0] - 1][bfsLocation[1]] = True
            q.append((bfsLocation[0] - 1, bfsLocation[1]))

        if (ground[bfsLocation[0]][bfsLocation[1] + 1] == '.') and (not visited[bfsLocation[0]][bfsLocation[1] + 1]):
            visited[bfsLocation[0]][bfsLocation[1] + 1] = True
            q.append((bfsLocation[0], bfsLocation[1] + 1))

        if (ground[bfsLocation[0]][bfsLocation[1] - 1] == '.') and (not visited[bfsLocation[0]][bfsLocation[1] - 1]):
            visited[bfsLocation[0]][bfsLocation[1] - 1] = True
            q.append((bfsLocation[0], bfsLocation[1] - 1))

    sol = sum([row.count('#') for row in ground])
    print(sol)

def part2():
    points = []
    instructions = []
    totalSteps = 0
    for line in open("input.txt"):
        line = line.strip().split()[2].strip("()")
        direction, steps = convertDir(line[-1]), int(line[1:-1], 16)
        instructions.append((direction, steps))
        
    location = (0,0)
    points.append(location)
    for instruction in instructions:
        direction = getDir(instruction[0])
        steps = instruction[1]
        totalSteps += steps
        location = (location[0] + steps * direction[0], location[1] + steps * direction[1])
        points.append(location)

    sum = 0
    for i in range(len(points) - 1):
        sum += points[i][0] * points[i + 1][1]
        sum -= points[i][1] * points[i + 1][0]
    
    print((int(totalSteps + 2 +abs(sum)) // 2))

part2()