import networkx as nx
def route(blocked=False):
    graph=nx.Graph()
    graph.add_weighted_edges_from([('A','B',4),('B','D',3),('A','C',5),('C','D',4),('B','C',2)])
    if blocked:
        graph.remove_edge('B','D')
    path=nx.shortest_path(graph,'A','D',weight='weight')
    return graph,path,nx.path_weight(graph,path,'weight')
