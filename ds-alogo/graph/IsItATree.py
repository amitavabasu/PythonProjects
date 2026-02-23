"""
Problem

Is It A Tree
Given an undirected graph, find out whether it is a tree.

The undirected edges are given by two arrays edge_start and edge_end of equal size. Edges of the given graph connect nodes edge_start[i] and edge_end[i] for all valid i.

Example One
Graph 1

{
"node_count": 4,
"edge_start": [0, 0, 0],
"edge_end": [1, 2, 3]
}
Output:

1
This graph is a tree because all the nodes are connected, and it does not have cycles.

Example Two
Graph 2

{
"node_count": 4,
"edge_start": [0, 0],
"edge_end": [1, 2]
}
Output:

0
This graph is not a tree because node 3 is not connected to the other nodes.

Example Three
Graph 3

{
"node_count": 4,
"edge_start": [0, 0, 1, 2],
"edge_end": [3, 1, 2, 0]
}
Output:

0
This graph is not a tree: nodes 0, 1 and 2 form a cycle.

Example Four
Graph 4

{
"node_count": 4,
"edge_start": [0, 0, 0, 1],
"edge_end": [1, 2, 3, 0]
}
Output:

0
This graph is not a tree because the two edges that connect nodes 0 and 1 form a cycle.

Notes
A tree is an undirected connected acyclic graph.
Constraints:

1 <= number of nodes <= 105
1 <= number of edges <= 105
0 <= node value < number of nodes
"""


def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    adj_list = [[] for _ in range(node_count)]
    for i in range(len(edge_start)):
        adj_list[edge_start[i]].append(edge_end[i])
        adj_list[edge_end[i]].append(edge_start[i])
    visited = [False] * node_count
    parent = [-1] * node_count
    component = 0
    for i in range(node_count):
        if visited[i] == False:
            component += 1
            if (component > 1): return False
            cycle = dfs_helper(adj_list, i, visited, parent)
            if cycle: return False
    return True


def dfs_helper(adj_list, s, visited, parent):
    visited[s] = True
    for v in adj_list[s]:
        if not visited[v]:
            parent[v] = s
            cycle = dfs_helper(adj_list, v, visited, parent)
            if cycle: return True
        else:
            if parent[s] != v:
                return True
    return False


if __name__ == "__main__":

    node_count = 4
    edge_start = [0, 0, 0]
    edge_end = [1, 2, 3]

    # node_count = 4
    # edge_start = [0, 0, 0, 1]
    # edge_end = [1, 2, 3, 0]

    # node_count = 4
    # edge_start = [0, 0]
    # edge_end = [1, 2]

    print(is_it_a_tree(node_count, edge_start, edge_end))