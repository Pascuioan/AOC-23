import time
def part1():
    sum = 0
    for line in open("input.txt"):
        line = line[8:]
        winningNums, nums =map(str.strip , line.split("|"))
        winningNums = set(winningNums.split())
        nums = set(nums.split())
        matchin = len(nums.intersection(winningNums))
        if matchin != 0:
            sum += 2**(matchin - 1)
    print(sum)

def part2():
    cards = {}
    card = 1
    for line in open("input.txt"):
        line = line[8:]
        winningNums, nums =map(str.strip , line.split("|"))
        winningNums = set(winningNums.split())
        nums = set(nums.split())
        matching = len(nums.intersection(winningNums))
        cards[card] = (1, matching)
        card += 1
    
    for card in cards.keys():
        value = cards[card]
        for i in range(card + 1, card + 1 + value[1]):
            cards[i] = (cards[i][0] + value[0], cards[i][1])
    
    sum = 0
    for card in cards.values():
        sum += card[0]
    print(sum)

start_time = time.time()
part2()
print("--- %s seconds ---" % (time.time() - start_time))