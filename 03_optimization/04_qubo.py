from itertools import product
# Ровно один объект из трёх. Максимизируем полезность.
values = [2,5,3]
penalty = 10
def objective(bits):
    return -sum(v*b for v,b in zip(values,bits)) + penalty*(sum(bits)-1)**2
if __name__ == '__main__':
    for bits in product([0,1],repeat=3):
        print(bits,objective(bits))
    best = min(product([0,1],repeat=3),key=objective)
    print('Минимум:',best,objective(best))
# Квадрат штрафа превращает ограничение в квадратичную функцию.
