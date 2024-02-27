from functools import cmp_to_key

def faceValue1(card):
    try:
        return int(card)
    except:
        if card == 'T':
            return 10
        if card == 'J':
            return 11
        if card == 'Q':
            return 12
        if card == 'K':
            return 13
        if card == 'A':
            return 14
        
def faceValue2(card):
    try:
        return int(card)
    except:
        if card == 'T':
            return 10
        if card == 'J':
            return 1
        if card == 'Q':
            return 12
        if card == 'K':
            return 13
        if card == 'A':
            return 14

def handType1(hand):
    d = {}
    for card in hand:
        if card in d:
            d[card] += 1
        else:
            d[card] = 1
    values = sorted(list(d.values()), reverse = True)
    if values == [5]:
        return 7
    if values == [4,1]:
        return 6
    if values == [3,2]:
        return 5
    if values == [3,1,1]:
        return 4
    if values == [2,2,1]:
        return 3
    if values == [2,1,1,1]:
        return 2
    return 1

def handType2(hand):
    d = {}
    for card in hand:
        if card in d:
            d[card] += 1
        else:
            d[card] = 1
    values = sorted(list(d.values()), reverse = True)
    jokers = 0
    if 'J' in d.keys():
        jokers = d['J']
        values.remove(jokers)

    if jokers == 5:
        values = [5]
    else: 
        values[0] += jokers

    if values == [5]:
        return 7
    if values == [4,1]:
        return 6
    if values == [3,2]:
        return 5
    if values == [3,1,1]:
        return 4
    if values == [2,2,1]:
        return 3
    if values == [2,1,1,1]:
        return 2
    return 1
    
def compareHands1(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    type1 = handType1(hand1)
    type2 = handType1(hand2)
    if type1 < type2:
        return 1
    if type1 > type2:
        return -1
    for i in range(5):
        value1 = faceValue1(hand1[i])
        value2 = faceValue1(hand2[i]) 
        if value1 < value2:
            return 1
        if value1 > value2:
            return -1
        
def compareHands2(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    type1 = handType2(hand1)
    type2 = handType2(hand2)
    if type1 < type2:
        return 1
    if type1 > type2:
        return -1
    for i in range(5):
        value1 = faceValue2(hand1[i])
        value2 = faceValue2(hand2[i]) 
        if value1 < value2:
            return 1
        if value1 > value2:
            return -1
        
def part1():
    hands = []
    for line in open("input.txt"):
        line = line.split()
        hands.append((line[0], int(line[1])))
    hands.sort(key = cmp_to_key(compareHands1), reverse = True)
    
    print(*hands[::-1], sep = '\n')

    sum = 0

    for i in range(len(hands)):
        sum += hands[i][1] * (i + 1)

    print(sum)

def part2():
    hands = []
    for line in open("input.txt"):
        line = line.split()
        hands.append((line[0], int(line[1])))
    hands.sort(key = cmp_to_key(compareHands2), reverse = True)
    
    print(*hands[::-1], sep = '\n')

    sum = 0

    for i in range(len(hands)):
        sum += hands[i][1] * (i + 1)

    print(sum)

part2()
