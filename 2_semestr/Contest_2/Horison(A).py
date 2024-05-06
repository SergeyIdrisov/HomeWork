"""
 Связный граф
Веса +-
Нужно найти отрицательный цикл
Алгоритм Форда-Белмона
Задача с неравенствами
"""
class Graph:
    def __init__(self, vertices):
        self.M = vertices
        self.graph = []
    def add_edge(self, a, b, c):
        self.graph.append([a, b, c])
    def print_solution(self):
        print("no")
    def bellman_ford(self, src):
        distance = [float("Inf")] * self.M
        distance[src] = 0
        for _ in range(self.M - 1):
            for a, b, c in self.graph:
                if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                    distance[b] = distance[a] + c
        for a, b, c in self.graph:
            if distance[a] != float("Inf") and distance[a] + c < distance[b]:
                print("yes")
                return
        self.print_solution()
n, m = map(int, input().split())
g = Graph(m)
for i in range(m):
    a, b, c = list(map(int, input().split()))
    g.add_edge(a, b, c)
try:
    g.bellman_ford(0)
except:
    print('no')