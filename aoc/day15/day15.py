from z3 import *


def main():
    lstX = []
    nodes = {}
    targetRow = 10
    # targetRow = 2000000
    count = 0

    with open("day15\\input.txt") as f:
        for line in f:
            line = line.strip().split()
            sens = (int(line[2][2:-1]), int(line[3][2:-1]))
            beac = (int(line[8][2:-1]), int(line[9][2:]))
            nodes[sens] = (beac, manhatten(sens,beac))
            # lstX.extend((beac[0], sens[0]))
            lstX.append(sens)
    lstX.sort()
    minX = lstX[0][0] - nodes[lstX[0]][1]
    maxX = lstX[-1][0] + nodes[lstX[-1]][1]
    print(minX,maxX)

    used = {}

    for x in nodes.values():
        if x[0][1] == targetRow:
            used[x[0][0]] = True

    x = Int('x')
    y = Int('y')
    s = z3.Solver()
    s.add(x <= 4000000)
    s.add(y <= 4000000)
    # s.add(x <= 20)
    # s.add(y <= 20)
    s.add(x >= 0)
    s.add(y >= 0)

    for sens in nodes:
        s.add(manhattenMod((x,y),sens) > nodes[sens][1])
        if manhatten(sens, (sens[0], targetRow)) <= nodes[sens][1]:
            for a in range(minX, maxX+1):
                if manhatten(sens, (a, targetRow)) <= nodes[sens][1]:
                    if not used.get(a, ''):
                        count +=1
                        used[a] = True
    print(count)
    s.check()
    m = s.model()
    solution = []
    for d in m.decls():
        solution.append((int("%s" % (m[d]))))
    print((solution[0] * 4000000 + solution[1]))


def customAbs(x):
    return If(x >= 0, x, -x)


def manhattenMod(a, b):
    return (customAbs(a[0]-b[0]) + customAbs(a[1]-b[1]))


def manhatten(a, b):
    return (abs(a[0] - b[0]) + (abs(a[1]-b[1])))


main()
