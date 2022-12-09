WIDTH = 99

def main():
    forest = [[None] * WIDTH for x in range(WIDTH)]
    x = 0
    with open("day8\\input.txt") as f:
        for line in f:
            line = line.strip()
            for y in range(WIDTH):
                forest[x][y] = int(line[y])
            x += 1
    count = 0
    max = 0
    for x in range(1, WIDTH-1):
        for y in range(1, WIDTH-1):
            if lookLeft(forest, x, y) or lookRight(forest, x, y) or lookUp(forest, x, y) or lookDown(forest, x, y):
                count+=1
            scenic = lookLeft2(forest, x, y) * lookRight2(forest, x, y) * lookUp2(forest, x, y) * lookDown2(forest, x, y)
            if scenic > max:
                max = scenic
            
    count += (WIDTH*4-4)
    print(count)
    print(max)


def lookLeft(forest, x, y):
    for a in range(y):
        current = forest[x][y]
        compare = forest[x][a]
        if forest[x][a] >= forest[x][y]:
            return False
    return True

def lookRight(forest, x, y):
    for a in range(y+1, WIDTH):
        current = forest[x][y]
        compare = forest[x][a]
        if forest[x][a] >= forest[x][y]:
            return False
    return True

def lookUp(forest, x, y):
    for a in range(x):
        current = forest[x][y]
        compare = forest[a][y] 
        if forest[a][y] >= forest[x][y]:
            return False
    return True

def lookDown(forest, x, y):
    for a in range(x+1, WIDTH):
        current = forest[x][y]
        compare = forest[a][y] 
        if forest[a][y] >= forest[x][y]:
            return False
    return True      

def lookLeft2(forest, x, y):
    a = y-1
    count = 0
    while(a >= 0):
        current = forest[x][y]
        compare = forest[x][a]
        count+=1
        if forest[x][a] >= forest[x][y]:
            break
        a-=1
    return count

def lookRight2(forest, x, y):
    a = y+1
    count = 0
    while(a < WIDTH):
        current = forest[x][y]
        compare = forest[x][a]
        count+=1
        if forest[x][a] >= forest[x][y]:
           break
        a+=1
    return count

def lookUp2(forest, x, y):
    a = x-1
    count = 0
    while(a >= 0):
        current = forest[x][y]
        compare = forest[x][a]
        count+=1
        if forest[a][y] >= forest[x][y]:
            break
        a-=1
    return count

def lookDown2(forest, x, y):
    a = x+1
    count = 0
    while(a < WIDTH):
        current = forest[x][y]
        compare = forest[x][a]
        count+=1
        if forest[a][y] >= forest[x][y]:
            break
        a+=1
    return count

def printForest(forest):
    for x in range(WIDTH):
        for y in range(WIDTH):
            print(forest[x][y],end='')
        print()

main()