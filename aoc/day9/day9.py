WIDTH = 50

def main():
    grid = [[None] * WIDTH for x in range(WIDTH)]
    x1, x2 = WIDTH-1, WIDTH-1
    y1, y2 = 0, 0
    head = grid[x1][y1]
    tail = grid[x2][y2]
    with open("day9\\input2.txt") as f:
        for line in f:
            line = line.strip().split()
            if line[0] == 'R':
                for x in range(int(line[1])):
                    y1+=1
                    head = grid[x1][y1]
                    if y1 - y2 > 1:
                        y2 += 1
                        tail = grid[x2][y2]
                        grid[x2][y2] = 1
            elif line[0] == 'L':
                for x in range(intline[1]):
                    y1-=1
                    head = grid[x1][y1]
                    if y2 - y1 > 1:
                        y2 -= 1
                        tail = grid[x2][y2]
                        grid[x2][y2] = 1


main()