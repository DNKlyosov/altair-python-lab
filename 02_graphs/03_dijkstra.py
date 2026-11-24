from heapq import heappop, heappush
import networkx as nx
G = nx.Graph()
G.add_weighted_edges_from([('A','B',4),('B','D',3),('A','C',5),('C','D',4),('B','C',2)])
def dijkstra(graph, start, end):
    queue = [(0,start,[start])]
    visited = set()
    while queue:
        cost,node,path = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        print('Посещаем',node,'стоимость',cost)
        if node == end:
            return cost,path
        for neighbor,attrs in graph[node].items():
            if neighbor not in visited:
                heappush(queue,(cost+attrs['weight'],neighbor,path+[neighbor]))
    return None
if __name__ == '__main__':
    print(dijkstra(G,'A','D'))
