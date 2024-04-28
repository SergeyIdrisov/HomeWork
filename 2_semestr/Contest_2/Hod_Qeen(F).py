"""
Алгоритм Эдмондса-Карпа
Соединим все вершины со всеми
В паросочетаниях нельзя брать смежные рёбра
Алгоритм Уна или потоки
Найти максимально паросочетание
"""
MAX = 301

g = [[0]*MAX for _ in range(MAX)]
used = []
par = []
mt = []
rows, cols, cuts, a, b, flow = 0, 0, 0, 0, 0, 0

def dfs(v):
    if used[v]:
        return 0
    used[v] = 1
    for to in range(cols):
        if g[v][to] == 0:
            continue
        if mt[to] == -1 or dfs(mt[to]):
            mt[to] = v
            par[v] = 1
            return 1
    return 0

def AugmentingPath():
    global rows, cols
    run = 1
    global mt, par, used
    mt = [-1]*cols
    par = [-1]*rows
    while run:
        run = 0
        used = [0]*rows
        for i in range(rows):
            if par[i] == -1 and dfs(i):
                run = 1
num = int(input())
for o in range(num):
    vvod = list(map(int, input().split()))
    if vvod != []:
        rows, cols, cuts = vvod[0], vvod[1], vvod[2]
        o-=1
        for i in range(rows):
            for j in range(cols):
                g[i][j] = 1
        c = list(map(int, input().split()))
        for j in range(cuts):
            g[c[2*j]][c[2*j+1]] = 0
        AugmentingPath()
        flow = sum(1 for i in range(cols) if mt[i] != -1)
        print(flow)
    else:
        continue