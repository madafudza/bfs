from collections import deque

graph = {0: [1, 2], 1: [0, 3], 2: [0, 4], 3: [1], 4: [2]}


def bfs(graph, start):
    distances = {vertex: -1 for vertex in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


# Пример вызова
result = bfs(graph, 0)
print(result)
