from enum import Enum

class direction(Enum):
        UP = (-1, 0)
        DOWN = (1, 0)
        RIGHT = (0, 1)
        LEFT = (0, -1)

def options(start, room):
    currentPipe = room[start[0]][start[1]]
    if currentPipe == '|':
        return direction.UP, direction.DOWN
    elif currentPipe == '-':
        return direction.RIGHT, direction.LEFT
    elif currentPipe == '7':
        return direction.LEFT, direction.DOWN
    elif currentPipe == 'J':
        return direction.LEFT, direction.UP
    elif currentPipe == 'F':
        return direction.RIGHT, direction.DOWN
    elif currentPipe == 'L':
        return direction.UP, direction.RIGHT
    else:
        direction1 = 0
        direction2 = 0
        up = room[max(start[0] - 1, 0)][start[1]]
        down = room[min(start[0] + 1, len(room) - 1)][start[1]]
        left = room[start[0]][max(start[1] - 1, 0)]
        right = room[start[0]][min(start[1] + 1, len(room[0]) - 1)]
        if up == '|' or up == '7' or up == 'F':
            direction1 = direction.UP
        if down == '|' or down == 'J' or down == 'L':
            if direction1 == 0:
                direction1 = direction.DOWN
            else:
                direction2 = direction.DOWN
        if right == '-' or right == 'J' or right == '7':
            if direction1 == 0:
                direction1 = direction.RIGHT
            else:
                direction2 = direction.RIGHT
        if left == '-' or left == 'J' or left =='F':
            direction2 = direction.LEFT
        return direction1, direction2

def step(location, dir):
    return (location[0] + dir.value[0], location[1] + dir.value[1])

def part1():
    room = []
    start = (0,0)
    for line in open("input.txt"):
        if 'S' in line:
            start = (len(room), line.index("S"))
        room.append(line)
    direction1, direction2 = options(start, room)
    current1 = current2 = start

    dist = 0
    while(True):
        dist += 1
        previous1 = current1
        previous2 = current2
        current1 = step(current1, direction1)
        if current1 == current2:
            break
        current2 = step(current2, direction2)
        if current1 == current2:
            break

        options1 = [*options(current1, room)]
        if previous1 == step(current1, options1[0]):
            options1 = options1[1]
        else:
            options1 = options1[0]

        options2 = [*options(current2, room)]
        if previous2 == step(current2, options2[0]):
            options2 = options2[1]
        else:
            options2 = options2[0]

        direction1 = options1
        direction2 = options2
            
    print(dist)

    
def part2():
    room = []
    steps = 0
    points = []
    start = (0,0)
    for line in open("input.txt"):
        if 'S' in line:
            start = (len(room), line.index("S"))
        room.append(line.strip())
    direction1, direction2 = options(start, room)

    if not (set([direction1, direction2]) == set([direction.UP, direction.DOWN])) or set([direction1, direction2]) == set([direction.RIGHT, direction.LEFT]):
        points.append(start)
    current1 = start

    while True:
        previous1 = current1
        current1 = step(current1, direction1)
        if current1 == start:
            break
        steps += 1

        pipe = room[current1[0]][current1[1]]
        if pipe != '|' and pipe != '-':
            points.append(current1)

        options1 = [*options(current1, room)]
        if previous1 == step(current1, options1[0]):
            options1 = options1[1]
        else:
            options1 = options1[0]

        direction1 = options1

    if points[0] == start:
        points.append(start)
    
    steps -= 1
 
    sum = 0
    for i in range(len(points) - 1):
        sum += points[i][0] * points[i + 1][1]
        sum -= points[i][1] * points[i + 1][0]
    
    # area = (int(steps + 2 +abs(sum)) // 2)
    print((abs(sum) - steps) // 2)

    # print(area - steps)
    
part2()