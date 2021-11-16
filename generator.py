from random import randint

import networkx as nx


def random_dag(nodes, edges):
    """Generate a random Directed Acyclic Graph with a given number of edges and nodes."""
    di_graph = nx.DiGraph()
    for i in range(nodes):
        di_graph.add_node(i)
    while edges > 0:
        a = randint(0, nodes - 1)
        b = a
        while b == a:
            b = randint(0, nodes - 1)
        di_graph.add_edge(a, b)
        if nx.is_directed_acyclic_graph(di_graph):
            edges -= 1
        else:
            di_graph.remove_edge(a, b)
    return di_graph


print("Enter the number of vertices and edges in numbers separated by a space:")

nodes, edges = [int(value) for value in input().split()]
graph = random_dag(nodes, edges)

graph_dict = {}
for edges in nx.edges(graph):
    graph_dict.update({edges[0]: [*graph_dict.get(edges[0], []), edges[1]]})

for node in nx.nodes(graph):
    if not graph_dict.get(node):
        graph_dict.update({node: []})

print("List of adjacent vertices: ", graph_dict)
