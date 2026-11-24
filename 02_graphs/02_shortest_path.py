import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_weighted_edges_from([('A','B',4),('B','D',3),('A','C',5),('C','D',4),('B','C',2)])
# Раскомментируйте следующую строку для эксперимента.
# G.remove_edge('B','D')
path = nx.shortest_path(G, 'A', 'D', weight='weight')
print('Маршрут:', path, 'Стоимость:', nx.path_weight(G,path,'weight'))
pos = {'A':(0,0),'B':(1,1),'C':(1,-1),'D':(2,0)}
nx.draw(G,pos,with_labels=True,node_color='lightblue')
nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
nx.draw_networkx_edges(G,pos,edgelist=list(zip(path,path[1:])),edge_color='green',width=3)
plt.show()
