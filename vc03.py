import networkx as nx
import matplotlib.pyplot as plt
import random
n = 10
m = 10
def printSubsets(vertices, current_subset, all_subsets, i):

    
    if i == len(vertices):
        all_subsets.append(current_subset.copy())
        return

    
    current_subset.append(vertices[i])

    printSubsets(vertices, current_subset, all_subsets, i + 1)

    
    current_subset.pop()

    
    printSubsets(vertices, current_subset, all_subsets, i + 1)


def min_Vertex_Cover(G, all_subsets):

    min_cover = None

    for subset in all_subsets:

        is_cover = True

        for u, v in G.edges():

            if u not in subset and v not in subset:

                is_cover = False
                break

        if is_cover:

            if min_cover is None or len(subset) < len(min_cover):

                min_cover = subset.copy()

    return min_cover

for m in range(m,46,5):

    G = nx.Graph()
    valid_edges = []

    i=0


    while i < m:

        u = random.randint(0, (n-1))
        v = random.randint(0, (n-1))

        if u != v:

            if (u, v) not in valid_edges and (v, u) not in valid_edges:
             i = i+1
             G.add_edge(u, v)
             valid_edges.append((u, v))


    vertices = list(G.nodes())
    all_subsets = []
    printSubsets(vertices, [], all_subsets, 0)
    min_cover = min_Vertex_Cover(G, all_subsets)

    print("Minimum Vertex Cover:", min_cover)
    print("Size:", len(min_cover))
    
    node_colors = []

    for node in G.nodes():
        if node in min_cover:
            node_colors.append("red")
        else:
            node_colors.append("skyblue")

    nx.draw(G, with_labels=True, node_color=node_colors)
    plt.show()