def getPatternValue1(pattern):
    i, j = 0, len(pattern) - 1
    while i < j:
        if pattern[i] == pattern[j]:
            ci, cj = i, j
            while i < j:
                if pattern[i] != pattern[j]:
                    break
                i += 1
                j -= 1
            else:
                if i - 1 == j:
                    return i * 100
            i = ci
            j = cj - 1
        else:
            j -= 1
    
    if i - 1 == j:
        return i * 100
    
    i, j = 0, len(pattern) - 1
    while i < j:
        if pattern[i] == pattern[j]:
            ci, cj = i, j
            while i < j:
                if pattern[i] != pattern[j]:
                    break
                i += 1
                j -= 1
            else:
                if i - 1 == j:
                    return i * 100
            i = ci + 1
            j = cj
        else:
            i += 1
    
    if i - 1 == j:
        return i * 100
    
    transposed = ["".join(s) for s in [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]]
    try:
        return int(getPatternValue1(transposed) / 100)
    except RuntimeError as e:
        return 0

def isSimilar(str1, str2):
    foundSmudge = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundSmudge:
                return 2
            else:
                foundSmudge = True
    
    if foundSmudge:
        return 1
    return 0
        

def getPatternValue2(pattern):
    i, j = 0, len(pattern) - 1
    smudgeFound = False
    while i < j:
        similarity = isSimilar(pattern[i], pattern[j])
        if similarity != 2:
            if similarity == 1:
                smudgeFound = True
            ci, cj = i, j
            i += 1
            j -= 1
            while i < j:
                sim = isSimilar(pattern[i], pattern[j])
                if sim == 2:
                    break
                if sim == 1 and smudgeFound:
                    break
                if sim == 1:
                    smudgeFound = True
                i += 1
                j -= 1
            else:
                if i - 1 == j and smudgeFound:
                    return i * 100
            i = ci
            j = cj - 1
            smudgeFound = False
        else:
            j -= 1
    
    if i - 1 == j and smudgeFound:
        return i * 100
    
    i, j = 0, len(pattern) - 1
    smudgeFound = False
    while i < j:
        similarity = isSimilar(pattern[i], pattern[j])
        if similarity != 2:
            if similarity == 1:
                smudgeFound = True
            ci, cj = i, j
            i += 1
            j -= 1
            while i < j:
                sim = isSimilar(pattern[i], pattern[j])
                if sim == 2:
                    break
                if sim == 1 and smudgeFound:
                    break
                if sim == 1:
                    smudgeFound = True
                i += 1
                j -= 1
            else:
                if i - 1 == j and smudgeFound:
                    return i * 100
            i = ci + 1
            j = cj
            smudgeFound = False
        else:
            i += 1
    
    if i - 1 == j and smudgeFound:
        return i * 100
    
    transposed = ["".join(s) for s in [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]]
    try:
        return int(getPatternValue2(transposed) / 100)
    except RuntimeError as e:
        return 0

def part1():
    sum = 0
    pattern = []
    f = open("input.txt")
    for line in f:
        if line.strip() != "":
            pattern.append(line.strip())
            continue
        
        sum += getPatternValue1(pattern)
        pattern = []

    sum += getPatternValue1(pattern)

    print(sum)

def part2():
    sum = 0
    pattern = []
    f = open("input.txt")
    for line in f:
        if line.strip() != "":
            pattern.append(line.strip())
            continue
        
        sum += getPatternValue2(pattern)
        pattern = []

    sum += getPatternValue2(pattern)

    print(sum)
        
part2()