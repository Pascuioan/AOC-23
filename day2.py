def part1():
    sum = 0
    for line in open("input.txt"):
        line = line.split(":")
        gameNum = int(line[0][5:])
        line = line[1].split(",")
        line = [(x.split(";")) for x in line]
        pairs = []
        for list in line:
            for pair in list:
                pair = pair.strip().split()
                pair = (int(pair[0]), pair[1])
                pairs.append(pair)
        for pair in pairs:
            if pair[0] > 12 and pair[1] == 'red':
                break
            if pair[0] > 13 and pair[1] == 'green':
                break
            if pair[0] > 14 and pair[1] == 'blue':
                break
        else:
            sum += gameNum
    print(sum)

def part2():
    sum = 0
    for line in open("input.txt"):
        maximum = {}
        maximum["green"] = 0
        maximum["blue"] = 0
        maximum["red"] = 0
        line = line.split(":")
        line = line[1].split(",")
        line = [(x.split(";")) for x in line]
        pairs = []
        for list in line:
            for pair in list:
                pair = pair.strip().split()
                pair = (int(pair[0]), pair[1])
                pairs.append(pair)
        for pair in pairs:
            maximum[pair[1]] = max(pair[0], maximum[pair[1]])
        sum += maximum["blue"]*maximum["green"]*maximum["red"]
    print(sum)
part2()