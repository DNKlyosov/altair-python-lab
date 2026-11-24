from itertools import product
edges = [(0,1),(0,2),(1,2),(1,3),(2,3)]
def score(bits):
    return sum(bits[a]!=bits[b] for a,b in edges)
if __name__ == '__main__':
    best = max(product([0,1],repeat=4),key=score)
    print('Группы:',best,'разрез:',score(best))
