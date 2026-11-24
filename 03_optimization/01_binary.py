from itertools import product
for bits in product([0,1], repeat=3):
    print(bits, 'выбрано:',sum(bits))
