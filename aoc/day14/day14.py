SIDE = 700
grid = [['.'] * SIDE for x in range(SIDE)]
dic = {}


def main():
    floor = 0
    with open("day14\\input2.txt") as f:
        for line in f:
            line = line.strip().split("->")
            for x in range(len(line)):
                line[x] = line[x].strip().split(',')
                line[x][0],line[x][1] = int(line[x][0]), int(line[x][1])
                if line[x][1] > floor:
                    floor = line[x][1]
            # drawRocks(line)
            drawDic(line)
    floor += 2
    dropSandDic(floor)
    # dropSand()
    print('Floor:', floor)
       

def dropSandDic(floor):
    count = 0
    hitSource = False
    row, col = 0, 500
    while not hitSource:
        if dic.get((0,500), '') != 'O':
            if row >= floor:
                dic[(row,col)] = 'O'
                row,col = 0,500
            if dic.get((row+1,col), '.') == '.':
                row += 1
            elif dic.get((row+1,col-1), '.') == '.':
                row, col = row+1, col-1
            elif dic.get((row+1,col+1), '.') == '.':
                row, col = row+1, col+1
            else:
                dic[(row,col)] = 'O'
                count+=1
                row, col = 0, 500
        else:
            hitSource = True
    print('Count dic', count)


def drawDic(line):
    for x in range(len(line)):
        line[x][0] = line[x][0]  # - 494

    for x in range(len(line)-1):
        start = line[x]
        end = line[x+1]
        row1,col1,row2,col2 = start[1],start[0],end[1],end[0]
        if row1 == row2:  # If x coords are same, increment through y
            if col1 < col2:  # If start y is smaller than end y
                for c in range(col1, col2+1):
                    dic[(row1,c)] = '#'
            if col1 > col2:
                for c in range(col2, col1+1):
                    dic[(row1,c)] = '#'
        if col1 == col2:
            if row1 < row2:
                for r in range(row1, row2+1):
                    dic[(r,col1)] = '#'
            if row1 > row2:
                for r in range(row2, row1+1):
                    dic[(r,col1)] = '#'


def dropSand():
    fellOff = False
    count = 0
    while not fellOff:
        count += 1
        fellOff = rMoveSand(0,500)
    print('Count:', count-1)


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
