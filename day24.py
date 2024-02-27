import math
# def cross_prod(a, b):
#     result = [a[1]*b[2] - a[2]*b[1],
#             a[2]*b[0] - a[0]*b[2],
#             a[0]*b[1] - a[1]*b[0]]

#     return result

# def intersect(l1, l2):
#     cp = cross_prod(l1[1], l2[1])
#     dif = [l1[0][0] - l2[0][0], l1[0][1] - l2[0][1], l1[0][2] - l2[0][2]]

#     if (dif == [0,0,0]) or (cp == 0):
#         return True

#     return False

def intersect(l1, l2):
    x1, y1, _ = l1[0]
    x2, y2, _ = l1[1]
    a1, b1, _ = l2[0]
    a2, b2, _ = l2[1]

    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (b2 - b1) / (a2 - a1)

    const1 = y1 - (x1 * slope1)
    const2 = b1 - (a1 * slope2)

    if math.isclose(slope1, slope2):
        # print("parallel")
        return False

    x = (const1 - const2) / (slope2 - slope1)
    y = x*x1 + y1

    # print(x, y)

    if x2 > x1:
        d1 = 'r'
    else:
        d1 = 'l'
    
    if a2 > a1:
        d2 = 'r'
    else:
        d2 = 'l'

    if (d1 == 'r') and (x < x1):
        return False
    if (d1 == 'l') and (x > x1):
        return False
    if (d2 == 'r') and (x < a1):
        return False
    if (d2 == 'l') and (x > a1):
        return False
    
    if (x <= 200000000000000) or (x >= 400000000000000):
        return False
    
    return True

def part1():
    lines = []
    for line in open("input.txt"):
        line = line.split("@")
        p1 = [int(x) for x in line[0].split(", ")]
        d = [int(x) for x in line[1]. split(", ")]
        p2 = [p1[i] + d[i] for i in range(3)]

        lines.append((p1,p2))

    intersections = 0

    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            if intersect(lines[i], lines[j]):
                intersections += 1
    print(intersections)

part1()