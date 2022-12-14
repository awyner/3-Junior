import networkx as nx

WIDTH = 70
HEIGHT = 41
# WIDTH = 8
# HEIGHT = 5

def main():
    grid = [[None] * WIDTH for x in range(HEIGHT)]
    row = 0
    start = ()
    end = ()
    lista = []
    with open("day12\\input.txt") as f:
       for line in f:
        line = line.strip()
        for col in range(len(line)):
            grid[row][col] = line[col]
            if grid[row][col] == 'S':
                grid[row][col] = 'a'
                start = (row,col)
            if grid[row][col] == 'E':
                grid[row][col] = 'z'
                end = (row,col)
            if grid[row][col] == 'a':
                lista.append((row,col))
        row+=1
    graph = nx.DiGraph()
    for row in range(HEIGHT):
        for col in range(WIDTH):
            graph = checkUp(row,col,grid,graph)
            graph = checkDown(row,col,grid,graph)
            graph = checkLeft(row,col,grid,graph)
            graph = checkRight(row,col,grid,graph)
    for a in range(len(lista)):    
        start = lista[a]
        try:
            lista[a] = nx.shortest_path_length(graph, start, end)
        except:
            lista[a] = 1_000_000_000
    lista.sort()
    print(lista[0])   

def checkUp(row,col,grid,graph):
    if row > 0:
        if ord(grid[row-1][col]) - ord(grid[row][col]) <= 1:
            graph.add_edge((row,col), (row-1,col))
    return graph

def checkDown(row,col,grid,graph):
    if row < HEIGHT-1:
        if ord(grid[row+1][col]) - ord(grid[row][col]) <= 1:
            graph.add_edge((row,col),(row+1,col))
    return graph

def checkLeft(row,col,grid,graph):
    if col > 0:
        if ord(grid[row][col-1])-ord(grid[row][col]) <= 1:
            graph.add_edge((row,col),(row,col-1))
    return graph

def checkRight(row,col,grid,graph):
    if col < WIDTH-1:
        if ord(grid[row][col+1])-ord(grid[row][col]) <= 1:
            graph.add_edge((row,col),(row,col+1))
    return graph


main()