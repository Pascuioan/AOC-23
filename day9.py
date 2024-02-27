def allZeros(list):
    for num in list:
        if num != 0:
            return False
    return True

def part1():
    sum = 0
    for line in open("input.txt"):
        steps = []
        line = [int(x) for x in line.split()]
        steps.append(line)
        while not allZeros(steps[-1]):
            steps.append([steps[-1][i + 1] - steps[-1][i] for i in range(len(steps[-1]) - 1)])
        
        for i in range(len(steps) - 2, -1, -1):
            steps[i].append(steps[i][-1] + steps[i + 1][-1])
    
        sum += steps[0][-1]

    print(sum)

def part2():
    sum = 0
    for line in open("input.txt"):
        steps = []
        line = [int(x) for x in line.split()]
        steps.append(line)
        while not allZeros(steps[-1]):
            steps.append([steps[-1][i + 1] - steps[-1][i] for i in range(len(steps[-1]) - 1)])
        
        for i in range(len(steps) - 2, -1, -1):
            steps[i].insert(0, steps[i][0] - steps[i + 1][0])
    
        print(steps)

        sum += steps[0][0]

    print(sum)

part2()