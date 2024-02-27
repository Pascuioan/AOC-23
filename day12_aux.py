def part1():
    pairs = []
    for line in open("input.txt"):
        pattern, nums = line.strip().split(maxsplit=1)
        # print(line.strip())
        pattern = pattern.strip(".")
        nums = [int(x) for x in nums.split(",")]
        pairs.append((pattern, nums))
    
    f = open("day12_input.txt", "w")
    f.write("t :: [(String,[Int])] = ")
    f.write(str(pairs))
    f.close()

    f = open("day12_input.txt", "r")
    line = f.readline()
    line = line.replace("'", "\"")
    f.close()
    f = open("day12_input.txt", "w")
    f.write(line)

def part2():
    pairs = []
    for line in open("input.txt"):
        pattern, nums = line.strip().split()
        pattern = pattern.strip(".")
        nums = [int(x) for x in nums.split(",")]
        # pairs.append((pattern, nums))
        print(pattern, end="")
        print("?", end="")
        print(pattern, end="")
        print("?", end="")
        print(pattern, end="")
        print("?", end="")
        print(pattern, end="")
        print("?", end="")
        print(pattern, end=" ")
        print(*nums, sep = ",")
    

part1()