from itertools import product
items = [('Ноутбук',3,9),('Камера',2,6),('Аккумулятор',4,10),('Инструменты',2,4),('Аптечка',1,3)]
def solve(capacity):
    best = (0,0,[])
    for bits in product([0,1], repeat=len(items)):
        selected = [item for item,b in zip(items,bits) if b]
        weight = sum(i[1] for i in selected)
        value = sum(i[2] for i in selected)
        if weight <= capacity and value > best[0]:
            best = (value,weight,selected)
    return best
if __name__ == '__main__':
    print('Полезность, вес, предметы:',solve(7))
