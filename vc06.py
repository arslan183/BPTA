import networkx as nx
import matplotlib.pyplot as plt
import random
import time

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


for m in range(m, 46, 5):

    G = nx.Graph()
    valid_edges = []

    i = 0

    while i < m:

        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)

        if u != v:

            if (u, v) not in valid_edges and (v, u) not in valid_edges:

                i += 1
                G.add_edge(u, v)
                valid_edges.append((u, v))




    input_filename = f"inputN{n}M{m}.txt"

    with open(input_filename, "w") as f:

        f.write(f"n = {n}, m = {m}\n")

        for u, v in valid_edges:
            f.write(f"{u} {v}\n")




    G = nx.Graph()

    with open(input_filename, "r") as f:

        for line in f:

            line = line.strip()

            if line.startswith("n ="):

                parts = line.split(",")

                n_read = int(parts[0].split("=")[1])
                m_read = int(parts[1].split("=")[1])

                G.add_nodes_from(range(n_read))

            else:

                u, v = map(int, line.split())

                G.add_edge(u, v)



    vertices = list(G.nodes())

    start_time = time.perf_counter()

    all_subsets = []

    printSubsets(vertices, [], all_subsets, 0)

    min_cover = min_Vertex_Cover(G, all_subsets)

    end_time = time.perf_counter()

    running_time = end_time - start_time

    print(f"Running time is {running_time}")


    output_filename = f"outputN{n}M{m}.txt"

    with open(output_filename, "w") as f:

        f.write(f"n = {n_read}\n")
        f.write(f"m = {m_read}\n")
        f.write(f"Minimum Vertex Cover: {min_cover}\n")
        f.write(f"Size: {len(min_cover)}\n")
        f.write(f"Running time is {running_time}\n")


    print("Minimum Vertex Cover:", min_cover)
    print("Size:", len(min_cover))


    node_colors = []

    for node in G.nodes():

        if node in min_cover:
            node_colors.append("red")
        else:
            node_colors.append("skyblue")


    nx.draw(G, with_labels=True, node_color=node_colors)

    image_filename = f"graphN{n}M{m}.png"

    plt.savefig(image_filename)

    plt.show()

    plt.close()