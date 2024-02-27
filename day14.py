import copy

def rollNorth(floor):
    for i in range(1, len(floor)):
        for j in range(len(floor[0])):
            if floor[i][j] == 'O':
                heighest = i
                while heighest > 0 and floor[heighest - 1][j] == '.':
                    heighest -= 1
                floor[i][j] = '.'
                floor[heighest][j] = 'O'
    
    return floor

def rollSouth(floor): 
    for i in range(len(floor) - 2, -1, -1):
        for j in range(len(floor[0])):
            if floor[i][j] == 'O':
                lowest = i
                while lowest < (len(floor) - 1) and floor[lowest + 1][j] == '.':
                    lowest += 1
                floor[i][j] = '.'
                floor[lowest][j] = 'O'
    
    return floor

def rollEast(floor): 
    for j in range(len(floor[0]) - 2, -1, -1):
        for i in range(len(floor)):
            if floor[i][j] == 'O':
                eastMost = j
                while eastMost < (len(floor[0]) - 1) and floor[i][eastMost + 1] == '.':
                    eastMost += 1
                floor[i][j] = '.'
                floor[i][eastMost] = 'O'
    
    return floor

def rollWest(floor): 
    for j in range(len(floor[0])):
        for i in range(len(floor)):
            if floor[i][j] == 'O':
                westMost = j
                while westMost > 0 and floor[i][westMost - 1] == '.':
                    westMost -= 1
                floor[i][j] = '.'
                floor[i][westMost] = 'O'
    
    return floor

def part1():
    floor = []
    for line in open("input.txt"):
        floor.append(list(line.strip()))
    
    floor = rollNorth(floor)

    height = len(floor)
    sum = 0
    for ind, f in enumerate(floor):
        sum += f.count('O') * (height - ind)

    print(sum)

def part2():
    floor = []
    for line in open("input.txt"):
        floor.append(list(line.strip()))
    
    phases = []


    floor = rollNorth(floor)
    floor = rollWest(floor)
    floor = rollSouth(floor)
    floor = rollEast(floor)

    phases.append(copy.deepcopy(floor))
    for i in range(1000000000):
        floor = rollNorth(floor)
        floor = rollWest(floor)
        floor = rollSouth(floor)
        floor = rollEast(floor)
        
        if floor in phases:
            break

        phases.append(copy.deepcopy(floor))

    index = phases.index(floor)
    phasesIndex = len(phases) - 1
    print("Phases: ", len(phases))
    print("First repetition: ", index)
    print((1000000000 - index) % (phasesIndex - index + 1))

    floor = phases[index + ((999999999 - index) % (phasesIndex - index + 1))]

    sum = 0
    for ind, f in enumerate(floor):
        sum += f.count('O') * (len(floor) - ind)
    print("Sum: ", sum)



part2()