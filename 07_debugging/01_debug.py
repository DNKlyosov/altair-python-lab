# Поставьте точку останова на строке total += weight.
weights=[4,3,2]
total=0
for weight in weights:
    total += weight
    print('Промежуточная сумма:',total)
assert total==9
