WIDTH = 5

def main():
    forest = [[None] * 5 for x in range(5)]
    
    x = 0
    with open("day8\\input2.txt") as f:
        for line in f:
            line = line.strip()
            for y in range(WIDTH):
                forest[x][y] = int(line[y])
            x += 1
    printForest(forest)
    for x in range(1, WIDTH):
        for y in range(1, WIDTH):
            current = forest[x][y]
            for z in range(0, x, -1):
                if forest[x][z] < current:
                    pass
                

def printForest(forest):
    for x in range(WIDTH):
        for y in range(WIDTH):
            print(forest[x][y],end='')
        print()

main()