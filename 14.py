# Дан связный взвешенный неориентированный граф. Рассмотрим пару вершин, расстояние между которыми максимально среди всех пар вершин. 
# Расстояние между ними называется диаметром графа. Эксцентриситетом вершины v называется максимальное расстояние от вершины 
# v до других вершин графа. Радиусом графа называется наименьший из эксцентриситетов вершин. Найдите диаметр и радиус графа.

# Формат ввода
# В первой строке входного файла единственное число: N (1≤N≤100) — количество вершин графа. В следующих N строках по N
# чисел — матрица смежности графа, где -1 означает отсутствие ребра между вершинами, а любое неотрицательное число — присутствие 
# ребра данного веса. На главной диагонали матрицы всегда нули; веса рёбер не превышают 1000.

# Формат вывода
# В выходной файл выведите два числа — диаметр и радиус графа.

def shortest_paths(matrix, n):
    dist = [[0 if i == j else matrix[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != -1 and dist[k][j] != -1:
                    if dist[i][j] == -1 or dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def diameter_radius(dist):
    d = -1
    r = float('inf')

    for i in range(len(dist)):
        max_dist = max(dist[i])
        if max_dist != -1:
            r = min(r, max_dist)
            d = max(d, max_dist)

    return d, r

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dist = shortest_paths(matrix, n)

d, r = diameter_radius(dist)

print(d)
print(r)