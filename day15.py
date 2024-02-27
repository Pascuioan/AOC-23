def hash(string):
    sum = 0
    for c in string:
        sum += ord(c)
        pSum = sum
        sum = sum << 4
        sum += pSum
        sum = sum & 0xFF
    
    return sum

def part1():
    print(sum(list(map(hash, open("input.txt").readline().strip().split(",")))))

def part2():
    steps = open("input.txt").readline().strip().split(",")
    boxes = {}

    for step in steps:
        if '-' in step:
            lens = step[:-1]
            box = hash(lens)
            if box not in boxes.keys():
                continue
            for l in boxes[box]:
                if l[0] == lens:
                    boxes[box].remove(l)
                    break
        else:
            step = step.split("=")
            lens = step[0]
            box = hash(lens)
            focalLen = int(step[1])
            if box not in boxes.keys():
                boxes[box] = []
            for ind, l in enumerate(boxes[box]):
                if l[0] == lens:
                    boxes[box][ind] = (lens, focalLen)
                    break
            else:
                boxes[box].append((lens, focalLen))
    
    sum = 0

    for i in list(boxes.keys()):
        if boxes[i] == []:
            boxes.pop(i)
            continue
        for ind, lens in enumerate(boxes[i]):
            sum += (i + 1) * (ind + 1) * lens[1]
    
    print(boxes)
    print(sum)
        

part2()