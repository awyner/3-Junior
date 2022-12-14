SIDE = 700
grid = [['.'] * SIDE for x in range(SIDE)]
dic = {}


def main():
    maxY = 0
    with open("day14\\input.txt") as f:
        for line in f:
            line = line.strip().split("->")
            for x in range(len(line)):
                line[x] = line[x].strip().split(',')
                line[x][0],line[x][1] = int(line[x][0]), int(line[x][1])
                if line[x][0] > maxY:
                    maxY = line[x][0]
            drawRocks(line)
        print(maxY*2)
    dropSand()
    # for x in range(SIDE):
    #     for y in range(SIDE):
    #         print(grid[x][y], end=' ')
    #     print()
    

def dropSand():
    fellOff = False
    count = 0
    while not fellOff:
        count += 1
        fellOff = rMoveSand(0,500)
    print(count-1)


def rMoveSand(row, col):
    try:
        if grid[row+1][col] == '.':
            return rMoveSand(row+1,col)
        elif grid[row+1][col-1] == '.':
            return rMoveSand(row+1,col-1)
        elif grid[row+1][col+1] == '.':
            return rMoveSand(row+1,col+1)
        else:
            grid[row][col] = 'O'
    except IndexError:
        return True
                

def drawRocks(line):
    for x in range(len(line)):
        line[x][0] = line[x][0]  # - 494

    for x in range(len(line)-1):
        start = line[x]
        end = line[x+1]
        row1,col1,row2,col2 = start[1],start[0],end[1],end[0]
        if row1 == row2:  # If x coords are same, increment through y
            if col1 < col2:  # If start y is smaller than end y
                for c in range(col1, col2+1):
                    grid[row1][c] = '#'
            if col1 > col2:
                for c in range(col2, col1+1):
                    grid[row1][c] = '#'
        if col1 == col2:
            if row1 < row2:
                for r in range(row1, row2+1):
                    grid[r][col1] = '#'
            if row1 > row2:
                for r in range(row2, row1+1):
                    grid[r][col1] = '#'


main()
