import networkx as nx
import matplotlib.pyplot as plt


def main():
    graph = nx.Graph()
    n = []
    flow = {}
    with open("day16\\input2.txt") as f:
        for line in f:
            line = line.strip().split()
            n.append([line[1], line[9:]])
            graph.add_node(line[1])
            flow[line[1]] = int(line[4][5:-1])
    for node in n:
        if graph.has_node(node[0]):
            for x in node[1]:
                graph.add_edge(node[0], x)
    for v, items in graph.adjacency():
        print(items)
        for i in items:
            print(i,end='')
        print()


main()
