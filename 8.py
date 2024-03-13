# Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.

# Формат ввода
# В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S, F≤N), где N – количество вершин графа, 
# S – начальная вершина, а F – конечная. В следующих N строках вводится по N чисел, не превосходящих 100, 
# – матрица смежности графа, где -1 означает отсутствие ребра между вершинами, а любое неотрицательное 
# число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

# Формат вывода
# Требуется вывести последовательно все вершины одного (любого) из кратчайших путей, или одно число -1, если пути между указанными вершинами не существует. Пример выходного файла ниже неправильный. Правильный пример: 2 3 1.

N, S, F = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

S -= 1
F -= 1
MAX = float('inf')
dist = [MAX] * N
dist[S] = 0
visited = [False] * N
result = [-1] * N

for _ in range(N):
    min_dist = MAX
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
                result[i] = cur

if dist[F] != MAX:
    res = [];
    node = F
    while node != -1:
        res.append(node + 1)
        node = result[node]

    res.reverse()
    print(*res)
else:
    print(-1)
