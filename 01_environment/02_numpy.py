import numpy as np
# Каждая строка — координаты точки (x, y).
points = np.array([[0, 0], [3, 4], [6, 4]])
delta = points[1:] - points[:-1]
distances = np.linalg.norm(delta, axis=1)
print('Векторы перемещения:', delta)
print('Длины участков:', distances)
print('Общая длина:', distances.sum())
