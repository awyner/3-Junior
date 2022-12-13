# WIDTH = 30
WIDTH = 1_000

def main():
    grid = [[0] * WIDTH for x in range(WIDTH)]
    # coords = [[15,11],[15,11],[15,11],[15,11],[15,11],[15,11],[15,11],[15,11],[15,11],[15,11]]
    coords = [[WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2], [WIDTH//2,WIDTH//2]]
    # grid[15][11] = 1
    grid[coords[0][0]][coords[0][1]] = 1
    with open("day9\\input.txt") as f:
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
                            head,tail = checkDiag(head,tail)
                            head[1], tail[1] = check(head[1],tail[1])
                            head[0], tail[0] = check(head[0],tail[0])
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'L':
                    for x in range(line[1]):
                        coords[0][1] -= 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            head,tail = checkDiag(head,tail)
                            head[1], tail[1] = check(head[1],tail[1])
                            head[0], tail[0] = check(head[0],tail[0])
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'U':
                    for x in range(line[1]):
                        coords[0][0] -= 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            head,tail = checkDiag(head,tail)
                            head[1], tail[1] = check(head[1],tail[1])
                            head[0], tail[0] = check(head[0],tail[0])
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
                case 'D':
                    for x in range(line[1]):
                        coords[0][0] += 1
                        for a in range(9):
                            head = coords[a]
                            tail = coords[a+1]
                            head,tail = checkDiag(head,tail)
                            head[1], tail[1] = check(head[1],tail[1])
                            head[0], tail[0] = check(head[0],tail[0])
                            if a == 8:
                                grid[tail[0]][tail[1]] = 1
            #printGrid(grid)
            # print(coords)
                
    count = 0
    for x in range(WIDTH):
        for y in range(WIDTH):
            if grid[x][y]: 
                count += grid[x][y]
            print(grid[x][y], end = ' ')
        print()
    print(count)

def check(a, b):
    if a - b > 1:
        b +=1
    if b - a > 1:
        b -=1
    return a, b

def checkDiag(coords1, coords2):
    x1,y1,x2,y2 = coords1[0],coords1[1],coords2[0],coords2[1]
    if x1 - x2 >= 1 and y1 - y2 >= 2:
        x2+=1
        y2+=1
    elif x2 - x1 >= 1 and y1-y2 >= 2:
        x2-=1
        y2+=1
    elif x1-x2 >= 1 and y2-y1 >= 2:
        x2+=1
        y2-=1
    elif x2-x1 >= 1 and y2-y1 >= 2:
        x2-=1
        y2-=1
    elif x1 - x2 >= 2 and y1 - y2 >= 1:
        x2+=1
        y2+=1
    elif x2 - x1 >= 2 and y1-y2 >= 1:
        x2-=1
        y2+=1
    elif x1-x2 >= 2 and y2-y1 >= 1:
        x2+=1
        y2-=1
    elif x2-x1 >= 2 and y2-y1 >= 1:
        x2-=1
        y2-=1
    coords2[0],coords2[1]=x2,y2
    return coords1, coords2

def printGrid(grid):
    for x in range(WIDTH):
        for y in range(WIDTH):
            print(grid[x][y], end = ' ')
        print()
    print()
            
                

main()