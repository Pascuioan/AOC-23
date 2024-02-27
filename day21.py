import copy

def neighbours(coord, height, width):
    s = set()
    s.add((max(coord[0] - 1, 0), coord[1]))
    s.add((min(coord[0] + 1, height - 1), coord[1]))
    s.add((coord[0], max(coord[1] - 1, 0)))
    s.add((coord[0], min(coord[1] + 1, width - 1)))
    s.discard(coord)
    return list(s)

def part1():
    gardenTemplate = []
    steps = 64
    for line in open("input.txt"):
        if 'S' in line:
            start = (line.index('S'), len(gardenTemplate))
        gardenTemplate.append(line.strip())
    gardenTemplate = [[c for c in row] for row in gardenTemplate]
    gardenTemplate[start[0]][start[1]] = '.'
    
    garden = copy.deepcopy(gardenTemplate)
    garden[start[0]][start[1]] = 'O'

    for _ in range(steps):
        newGarden = copy.deepcopy(gardenTemplate)
        for i, row in enumerate(garden):
            for j, c in enumerate(row):
                if c == 'O':
                    for next in neighbours((i,j), len(garden), len(garden[0])):
                        if newGarden[next[0]][next[1]] == '.':
                            newGarden[next[0]][next[1]] = 'O'
        garden = newGarden

    sol = sum([row.count('O') for row in garden])
    print(sol)

part1()