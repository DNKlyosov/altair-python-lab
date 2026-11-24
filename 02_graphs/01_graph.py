import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([('A','B'), ('B','D'), ('A','C'), ('C','D'), ('B','C')])
print('Вершины:', list(G.nodes))
print('Соседи B:', list(G.neighbors('B')))
nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True)
plt.show()
