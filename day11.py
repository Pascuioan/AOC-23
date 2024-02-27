def emptySpaceBetween(low, high, nums):
    if low > high:
        low, high = high, low
    return len([x for x in nums if x < high and x > low])

def distance(galaxy1, galaxy2, emptyRows, emptyColumns):
    emptyRowsBetween = emptySpaceBetween(galaxy1[0], galaxy2[0], emptyRows)
    emptyColumnsBetween = emptySpaceBetween(galaxy1[1], galaxy2[1], emptyColumns)
    height = abs(galaxy1[0] - galaxy2[0]) + emptyRowsBetween * (emptySpaceMultiplier - 1)
    width = abs(galaxy1[1] - galaxy2[1]) + emptyColumnsBetween * (emptySpaceMultiplier - 1)

    return height + width


def part1():
    f = open("input.txt")
    universe = [f.readline().strip()]
    emptyRows = []
    galaxies = []
    emptyColumns = [True for _ in range(len(universe[0]))]
    if '#' not in universe[0]:
        emptyRows.append(0)
    for line in open("input.txt"):
        universe.append(line.strip())
        isEmpty = True
        for ind, ch in enumerate(line):
            if ch == '#':
                galaxies.append((len(universe) - 2, ind))
                emptyColumns[ind] = False
                isEmpty = False
        if isEmpty:
            emptyRows.append(len(universe) - 2)

    emptyColumns = [ind for ind, value in enumerate(emptyColumns) if value]

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i, len(galaxies)):
            sum += distance(galaxies[i], galaxies[j], emptyRows, emptyColumns)
    
    print(sum)

emptySpaceMultiplier = 1000000

part1()
