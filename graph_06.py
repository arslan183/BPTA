import networkx as nx
import matplotlib.pyplot as plt
n = int(input("Enter the no. of vertices: "))

while True:
    m = int(input("Enter the no. of edges: "))
    if m <(n-1) or m> n*(n-1)/2:
        print("invalid no. of edges for a connected graph")
    else:
        break


G=nx.Graph()

i=0

while i<m:
    print(f"{i+1}st edge")
    u= int(input("Enter the first node: "))
    v= int(input("Enter the second node: "))
    G.add_edge(u,v)
    i=i+1



nx.draw(G,with_labels=True)

plt.show()