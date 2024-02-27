def mapSeed(seed, maps):
    for map in maps:
        if seed >= map[1] and seed <= map[1] + map[2]:
            return map[0] + seed - map[1]
    return seed

def mapBlock(seedBlock, maps):
    start, end = seedBlock
    blocks = []
    for src, dest in maps:
        offset = dest[0] - src[0]
        if src[1] < start or end < src[0]:#disjunct
            continue
        elif src[0] > start and src[1] <= end:
            blocks.append((start, src[0] - 1))
            blocks.append((src[0] + offset, src[1] + offset))
            start = src[1] + 1
        elif src[0] > start and src[1] > end:
            blocks.append((start, src[0] - 1))
            blocks.append((src[0] + offset, end + offset))
            start = src[1]
        elif src[0] <= start and src[1] <= end:
            blocks.append((start + offset, src[1] + offset))
            start = src[1] + 1
        elif src[0] <= start and src[1] > end:
            blocks.append((start + offset, end + offset))
            start = end + 1
        if start > end:
           break
            
    if start <= end:
        blocks.append((start, end))
    return blocks

def uniteBlocks(blocks):
    changed = True
    while(changed):
        blocks = set(blocks)
        changed = False
        for start1, end1 in blocks:
            for start2, end2 in blocks:
                if start1 == start2 and end1 == end2:
                    continue
                if start1 > start2 and start1 < end2:
                    newInterval = (start2, max(end1, end2))
                    blocks.remove((start1, end1))
                    blocks.remove((start2, end2))
                    blocks.add(newInterval)
                    changed = True
                    break
            if changed:
                break
    return list(blocks)
        


def sortMaps(x):
    return x[0][1]

def part1():
    seeds = []
    toSoil = []
    toFertilizer = []
    toWater = []
    toLight = []
    toTemperature = []
    toHumidity = []
    toLocation = []
    next = -1
    for line in open("input.txt"):
        if line == "\n":
            continue
        elif "seeds" in line:
            line = line.split(maxsplit=1)
            seeds = [int(x) for x in line[1].split()]
            continue
        elif "to-soil" in line:
            next = 1
            continue
        elif "to-fertilizer" in line:
            next = 2
            continue
        elif "to-water" in line:
            next = 3
            continue
        elif "to-light" in line:
            next = 4
            continue
        elif "to-temperature" in line:
            next = 5
            continue
        elif "to-humidity" in line:
            next = 6
            continue
        elif "to-location" in line:
            next = 7
            continue
        
        match next:
            case 1:
                toSoil.append(tuple([int(x) for x in line.split()]))
            case 2:
                toFertilizer.append(tuple([int(x) for x in line.split()]))
            case 3:
                toWater.append(tuple([int(x) for x in line.split()]))
            case 4:
                toLight.append(tuple([int(x) for x in line.split()]))
            case 5:
                toTemperature.append(tuple([int(x) for x in line.split()]))
            case 6:
                toHumidity.append(tuple([int(x) for x in line.split()]))
            case 7:
                toLocation.append(tuple([int(x) for x in line.split()]))

    seeds = [mapSeed(seed, toSoil) for seed in seeds]
    seeds = [mapSeed(seed, toFertilizer) for seed in seeds]
    seeds = [mapSeed(seed, toWater) for seed in seeds]
    seeds = [mapSeed(seed, toLight) for seed in seeds]
    seeds = [mapSeed(seed, toTemperature) for seed in seeds]
    seeds = [mapSeed(seed, toHumidity) for seed in seeds]
    seeds = [mapSeed(seed, toLocation) for seed in seeds]

    print(min(seeds))

def part2():
    seedBlocks = []
    toSoil = []
    toFertilizer = []
    toWater = []
    toLight = []
    toTemperature = []
    toHumidity = []
    toLocation = []
    next = -1
    for line in open("input.txt"):
        if line == "\n":
            continue
        elif "seeds" in line:
            line = line.split(maxsplit=1)
            line = [int(x) for x in line[1].split()]
            for i in range(0, len(line), 2):
                seedBlocks.append((line[i], line[i] + line[i + 1]))
            continue
        elif "to-soil" in line:
            next = 1
            continue
        elif "to-fertilizer" in line:
            next = 2
            continue
        elif "to-water" in line:
            next = 3
            continue
        elif "to-light" in line:
            next = 4
            continue
        elif "to-temperature" in line:
            next = 5
            continue
        elif "to-humidity" in line:
            next = 6
            continue
        elif "to-location" in line:
            next = 7
            continue
        
        match next:
            case 1:
                map = [int(x) for x in line.split()]
                toSoil.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toSoil.sort(key = sortMaps)
            case 2:
                map = [int(x) for x in line.split()]
                toFertilizer.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toFertilizer.sort(key = sortMaps)
            case 3:
                map = [int(x) for x in line.split()]
                toWater.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toWater.sort(key = sortMaps)
            case 4:
                map = [int(x) for x in line.split()]
                toLight.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toLight.sort(key = sortMaps)
            case 5:
                map = [int(x) for x in line.split()]
                toTemperature.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toTemperature.sort(key = sortMaps)
            case 6:
                map = [int(x) for x in line.split()]
                toHumidity.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toHumidity.sort(key = sortMaps)
            case 7:
                map = [int(x) for x in line.split()]
                toLocation.append(((map[1], map[1] + map[2] - 1),(map[0], map[0] + map[2] - 1)))
                toLocation.sort(key = sortMaps)

    colletionOfMaps = [toSoil, toFertilizer, toWater, toLight, toTemperature, toHumidity, toLocation]

    for maps in colletionOfMaps:
        newSeedBlocks = []
        for block in seedBlocks:
            newSeedBlocks.extend(mapBlock(block, maps))
        seedBlocks = uniteBlocks(newSeedBlocks)

    seedBlocks = [x[0] for x in seedBlocks]
    print(min(seedBlocks))

part2()