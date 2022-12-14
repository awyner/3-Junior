SIDE = 10


def main():
    with open("day14\\input2.txt") as f:
        grid = ['.' * SIDE for x in range(SIDE)]
        for line in f:
            line = line.strip().split("->")
            for x in range(len(line)):
                line[x] = line[x].strip().split(',')
                line[x][0],line[x][1] = int(line[x][0]), int(line[x][1])
            grid = drawRocks(line, grid)
            # print(grid)


def drawRocks(line, grid):
    for x in range(len(line)-1):
        start = line[x]
        next = line[x+1]
        print(start, next)
    print()
    return line


main()
