# В ориентированном взвешенном графе вершины пронумерованы числами от 1 до n. Если i < j, то существует ребро из 
# вершины i в вершину j, вес которого определяется по формуле wt(i,j)=(179i+719j) mod 1000 - 500. 
# Определите вес кратчайшего пути, ведущего из вершины 1 в вершину n.

# Формат ввода
# Программа получает на вход одно число n (2 ≤ n ≤ 13000).

# Формат вывода
# Программа должна вывести единственное целое число - вес кратчайшего пути из вершины 1 в вершину n в описанном графе.

def shortest_path(n):
    dist = [float('infinity')] * (n + 1)
    dist[1] = 0

    for _ in range(n):
        updated = False
        for i in range(1, n + 1):
            for j in range(i + 1, min(i + 1000, n + 1)):
                weight = (179 * i + 719 * j) % 1000 - 500
                if dist[i] < float('infinity') and dist[i] + weight < dist[j]:
                    dist[j] = dist[i] + weight
                    updated = True
        if not updated:
            break

    return dist[n]

n = int(input())
print(shortest_path(n))
