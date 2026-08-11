import random
import networkx as nx
import matplotlib.pyplot as plt

n = 10
m = 10

fig, axes = plt.subplots(2, 4, figsize=(15, 8))
axes = axes.flatten()
grids = 0

for m in range(m,46,5):
    G = nx.Graph()


    valid_edges = []
    i=0
    while i<m:

        u = random.randint(0, (n-1))
        v = random.randint(0, (n-1))

        if(u!=v):
           
            if (u,v) not in valid_edges and (v,u) not in valid_edges:
                i=i+1
                G.add_edge(u , v)
                valid_edges.append((u, v))
    
    nx.draw(G, ax=axes[grids], with_labels=True)
    grids = grids+1
plt.show()




            
            
            
            
            
    
             


        

