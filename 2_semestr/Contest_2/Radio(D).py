"""
Надо немножко подумать
Самое тяжёлое ребро заменить спутником
Минимальное остовое дерево через Прим
Отсортировать по х слева направа и идти по точкам с меньшего к большему
и прибавлять к остову ближайшие точки
Берём n/2 последних рёбер и удаляем их.
Ответ: Самое тяжёлое оставшееся ребро.
"""
"""n = int(input())
v, u = map(int, input().split())
v /= 2
def MST():
    Edges = [[0,0,0]]
    for i in range(u):
        star = list(map(int, input().split()))
        weight = ((star[0]-Edges[i][-2])**2 + (star[1]-Edges[i][-1])**2)**0.5
        Edges.append([weight, star[0], star[1]])
    Edges.sort()
    print(Edges)
def Prim(G,u):
    INF = 10 ** 9
    dist = [INF] * u
    dist[0] = 0
    used = [False] * u
    ans = 0
    for i in range(u):
        min_dist = INF
        for j in range(u):
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        ans += min_dist
        used[u] = True
        for v in range(u):
            dist[v] = min(dist[v], W[u][v])
#print(f'{Edges[-1][0]:.{2}f}')
Tree = MST()
Prim(Tree,u)"""


def MST():
    Edges = [[0,0,0]]
    for i in range(u):
        star = list(map(int, input().split()))
        weight = ((star[0]-Edges[i][-2])**2 + (star[1]-Edges[i][-1])**2)**0.5
        Edges.append([weight, star[0], star[1]])
    Edges.sort()
    print(Edges)
    return Edges
def MIN(Edges):
    for i in range(int(v)):
        Edges.pop(-1)
    print(round(Edges[-1][0],2))
n = int(input())
for i in range(n):
    v, u = map(int, input().split())
    v /= 2
    Tree = MST()
    MIN(Tree)

"""import math
n = 0
x = []
y = []
used = []
dist = []
def dist2(i, j):
    return (x[j] - x[i]) * (x[j] - x[i]) + (y[j] - y[i]) * (y[j] - y[i])
def Prim():
    global n, dist, used
    dist = [float('inf')] * n
    used = [0] * n
    cur = 0
    dist[cur] = 0
    used[cur] = 1
    for i in range(1, n):
        for j in range(n):
            if used[j] == 0 and dist2(cur, j) < dist[j]:
                dist[j] = dist2(cur, j)
        min_dist = float('inf')
        for j in range(n):
            if used[j] == 0 and dist[j] < min_dist:
                min_dist = dist[j]
                cur = j
        used[cur] = 1
tests = int(input())
for _ in range(tests):
    s, n = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    Prim()
    dist.sort()
    answer_glav = round((dist[n - s])**0.5, 2)
    print(answer_glav)"""