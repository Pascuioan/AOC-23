import math

def winningTimes(time, distance):
    times = []
    delta = time * time - 4 * distance
    delta = math.sqrt(delta)
    x1 = (time + delta) / 2
    x2 = (time - delta) / 2
    rx2 = math.ceil(x2)
    rx1 = math.floor(x1)
    nums = rx1 - rx2 + 1
    if(x2 == rx2):
        nums -= 1
    if(x1 == rx1):
        nums -= 1
    return(nums)


def part1():
    f = open("input.txt")
    l1 = [int(x) for x in f.readline().split()[1:]]
    l2 = [int(x) for x in f.readline().split()[1:]]
    races = zip(l1,l2)
    solutions = [winningTimes(*race) for race in races]
    sol = 1
    for x in solutions:
        sol *= x
    print(sol)

def part2():
    f = open("input.txt")
    l1 = [x for x in f.readline().split()[1:]]
    l2 = [x for x in f.readline().split()[1:]]
    time = ""
    distance = ""
    for x in l1:
        time = time + x
    for x in l2:
        distance = distance + x
    print(winningTimes(int(time), int(distance)))

part2()
