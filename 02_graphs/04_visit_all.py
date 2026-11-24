from itertools import permutations
from math import dist
points = {'S':(0,0),'A':(2,1),'B':(4,0),'C':(1,4),'D':(4,4)}
def length(route):
    return sum(dist(points[a],points[b]) for a,b in zip(route,route[1:]))
routes = [('S',*order,'S') for order in permutations('ABCD')]
best = min(routes,key=length)
print('Проверено:',len(routes),'маршрутов')
print('Лучший:',best,'длина:',round(length(best),3))
# Это задача обхода всех точек, а не кратчайшего пути между двумя.
