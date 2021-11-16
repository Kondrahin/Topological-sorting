import ast
import time


def topological_sort(digraph):
    # digraph is a dictionary:
    #   key: a node
    # value: a set of adjacent neighboring nodes

    # construct a dictionary mapping nodes to their
    # indegrees
    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for neighbor in digraph[node]:
            indegrees[neighbor] += 1

    # track nodes with no incoming edges
    nodes_with_no_incoming_edges = []
    for node in digraph:
        if indegrees[node] == 0:
            nodes_with_no_incoming_edges.append(node)

    # initially, no nodes in our ordering
    topological_ordering = []

    # as long as there are nodes with no incoming edges
    # that can be added to the ordering
    while len(nodes_with_no_incoming_edges) > 0:
        # add one of those nodes to the ordering
        node = nodes_with_no_incoming_edges.pop()
        topological_ordering.append(node)

        # decrement the indegree of that node's neighbors
        for neighbor in digraph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                nodes_with_no_incoming_edges.append(neighbor)

    # we've run out of nodes with no incoming edges
    # did we add all the nodes or find a cycle?
    if len(topological_ordering) == len(digraph):
        return topological_ordering  # got them all
    else:
        print("Graph has a cycle! No topological ordering exists.")


print("Enter a list of adjacent vertices:")
digraph_str = input()
digraph = ast.literal_eval(digraph_str)

start_time = time.time()
sorting_result = topological_sort(digraph)
print(f"--- {(time.time() - start_time)} seconds ---")

print("Sorting result: ", sorting_result)

