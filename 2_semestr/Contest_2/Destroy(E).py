"""
Города - вершины
дороги - неориентированные рёбра
нужно удалить рёбра минимальной стоимостью и чтоб нельзя попасть из одной вершины в другую
Задача о минимальном разрезе
Минимальный разрез = максимальному потоку
"""
n = int(input())
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.org_graph = [i[:] for i in graph]
        self.ROW = len(graph)
        self.COL = len(graph[0])
        self.s = 0
    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return True if visited[t] else False
    def dfs(self, graph, s, visited):
        visited[s] = True
        for i in range(len(graph)):
            if graph[s][i] > 0 and not visited[i]:
                self.dfs(graph, i, visited)
    def minCut(self, source, sink):

        parent = [-1] * (self.ROW)
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            self.s = sink
            while (self.s != source):
                path_flow = min(path_flow, self.graph[parent[self.s]][self.s])
                self.s = parent[self.s]
            max_flow += path_flow
            v = sink
            while (v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        visited = len(self.graph) * [False]
        self.dfs(self.graph, self.s, visited)
        l,r = [],[]
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i] and not (visited[j]) and self.org_graph[i][j] > 0:
                    l.append(i)
                    r.append(j)
        return l,r
for i in range(n):
    g = []
    m = int(input())
    graph = [[]for _ in range(m)]
    for j in range(m):
        g.append(list(input()))
    for i in range(m):
        for j in range(m):
            graph[i].append(int(g[i][j]))
    for_answ = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for_answ[j].append(graph[j][i])

    l = []
    r = []
    for i in range(m):
        if i !=0:
            gra = [[0]*m for _ in range(m)]
            for o in range(len(graph)):
                for p in range(len(graph[o])):
                    gra[o][p] = graph[o][p]
            g = Graph(gra)
            a,b=g.minCut(0, i)
            l.append(a)
            r.append(b)
    ans = []
    for i in range(len(l)):
        answer = 0
        for j in range(len(l[i])):
            answer+=for_answ[l[i][j]][r[i][j]]
        ans.append(answer)
    print(min(ans))
