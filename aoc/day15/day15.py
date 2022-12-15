def main():
    lstX = []
    nodes = {}
    targetRow = 10
    targetRow = 2000000
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

    for sens in nodes:
        if manhatten(sens, (sens[0], targetRow)) <= nodes[sens][1]:
            for x in range(minX, maxX+1):
                if manhatten(sens, (x, targetRow)) <= nodes[sens][1]:
                    if not used.get(x, ''):
                        count +=1
                        used[x] = True
    print(count)


def manhatten(a, b):
    return (abs(a[0] - b[0]) + (abs(a[1]-b[1])))


main()
