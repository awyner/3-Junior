WIDTH = 30

def main():
    grid = [[0] * WIDTH for x in range(WIDTH)]
    # x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = WIDTH//2, WIDTH//2, WIDTH//2, WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2,WIDTH//2
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10 = 15,15,15,15,15,15,15,15,15,15,11,11,11,11,11,11,11,11,11,11
    coords = [[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5],[x6,y6],[x7,y7],[x8,y8],[x9,y9],[x10,y10]]
    grid[x2][y2] = 1
    with open("day9\\input2.txt") as f:
        for line in f:
            line = line.strip().split()
            line[1] = int(line[1])
            match line[0]:
                case 'R':
                    for x in range(line[1]):
                        coords[0][1] += 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            if checkDiag(head[0],tail[0],head[1],tail[1]):
                                head[0],tail[0],head[1],tail[1] = fixDiag(head[0],tail[0],head[1],tail[1])
                            elif checkY(head[1], tail[1]):
                                tail[1]+=1
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'L':
                    for x in range(line[1]):
                        coords[0][1] -= 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            if checkDiag(head[0],tail[0],head[1],tail[1]):
                                head[0],tail[0],head[1],tail[1] = fixDiag(head[0],tail[0],head[1],tail[1])
                            elif checkY(head[1],tail[1]):
                                tail[1]-=1
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'U':
                    for x in range(line[1]):
                        coords[0][0] -= 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            if checkDiag(head[0],tail[0],head[1],tail[1]):
                                head[0],tail[0],head[1],tail[1] = fixDiag(head[0],tail[0],head[1],tail[1])
                            elif checkX(head[0],tail[0]):
                                tail[0]-=1
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'D':
                    for x in range(line[1]):
                        coords[0][0] += 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            if checkDiag(head[0],tail[0],head[1],tail[1]):
                                head[0],tail[0],head[1],tail[1] = fixDiag(head[0],tail[0],head[1],tail[1])
                            elif checkX(head[0],tail[0]):
                                tail[0]+=1
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
            # printGrid(grid)
            # print(coords)
                
    count = 0
    for x in range(WIDTH):
        for y in range(WIDTH):
            if grid[x][y]: 
                count += grid[x][y]
            # print(grid[x][y], end = ' ')
        # print()
    print(count)

def checkY(y1, y2):
    return abs(y1-y2) > 1

def checkX(x1, x2):
    return abs(x1-x2) > 1

def checkDiag(x1, x2, y1, y2):
    if checkX(x1, x2) and abs(y1-y2) > 0:
        return True
    if abs(x1-x2) > 0 and checkY(y1, y2):
        return True
    return False

def fixDiag(x1,x2,y1,y2):
    if x1 > x2:
        x2+=1
    else:
        x2-=1
    if y1 > y2:
        y2+=1
    else:
        y2-=1
    return x1, x2, y1, y2

def printGrid(grid):
    for x in range(WIDTH):
        for y in range(WIDTH):
            print(grid[x][y], end = ' ')
        print()
            
                

main()