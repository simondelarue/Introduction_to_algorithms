"""
Created on October 2023
@author: Simon Delarue <sdelarue@enst.fr>
"""
import numpy as np


def bfs(g, s):
    ''' Breadth-first search algorithm. The algorithm attaches three additional attributes to each vertex:
        - its color ({white (0), grey (1), black (2)})
        - its distance from the source s
        - its predecessor in the breadth-first tree

    Parameters
    ----------
    g: List
        Graph encoded as a list of lists
    s: int
        Starting node index

    Returns
    -------
        Tuple of arrays
    '''
    n_nodes = len(g)
    V = set(range(n_nodes))
    Q = []

    # Initialisation of colors, distances and predecessors
    colors = np.zeros(n_nodes)
    distances = np.zeros(n_nodes)
    predecessors = np.zeros(n_nodes)

    colors[s] = 1

    Q.append(s)  # add source to queue

    while len(Q) != 0:
        u = Q.pop(0)
        # Search neighbors of u
        for v in g[u]:
            # Check if v is being discovered
            if colors[v] == 0:
                colors[v] = 1
                distances[v] = distances[u] + 1
                predecessors[v] = u
                # Add v to the frontier
                Q.append(v)
        # u is behind the frontier
        colors[u] = 2

    return (colors, distances, predecessors)
