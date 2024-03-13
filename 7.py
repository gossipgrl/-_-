# Дан ориентированный взвешенный граф.

# Найдите кратчайшее расстояние от одной заданной вершины до другой.

# Формат ввода
# В первой строке входного файла три числа: N, S и F (), где N — количество вершин графа, S — начальная вершина, 
# а F — конечная. В следующих N строках по N чисел — матрица смежности графа, где -1 означает отсутствие ребра 
# между вершинами, а любое целое неотрицательное число, не превосходящее 10000 — присутствие ребра данного веса. 
# На главной диагонали матрицы всегда нули.

# Формат вывода
# Вывести искомое расстояние или -1, если пути не существует.

import math

N, S, F = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

S -= 1
F -= 1
MAX = math.inf
dist = [MAX] * N;
dist[S] = 0
visited = [False] * N

for _ in range(N):
    min_dist = MAX;
    cur = -1
    for i in range(N):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            cur = i

    if cur == -1:
        break

    visited[cur] = True

    for i, weight in enumerate(matrix[cur]):
        if weight != -1:
            distance = dist[cur] + weight
            if distance < dist[i]:
                dist[i] = distance
if dist[F] != MAX:
    print(dist[F])
else:
    print(-1)