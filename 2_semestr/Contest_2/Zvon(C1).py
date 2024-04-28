"""
Минимальные остовные деревья
Тонкости:
Если не безопасному смежные только небезопасные - impossible
"""
N, M, p= map(int, input().split())
num = list(map(int, input().split()))
def MST():
    Edges = []
    for i in range(M):
        start, end, weight = map(int, input().split())
        Edges.append([weight, start, end])
    Edges.sort()
    return Edges
def MIN(Edges):
    Comp = [i for i in range(N)]
    Ans = 0
    visited = []
    shit = 0
    for weight, start, end in Edges:
        shit += 1
        if Comp[start-1] != Comp[end-1] and start not in visited:
            Ans += weight
            a = Comp[start-1]
            b = Comp[end-1]
            visited.append(start)
            for i in range(N):
                if Comp[i] == b:
                    Comp[i] = a
        if shit == M:
            visited.append(end)
    prov = []
    for i in range(N):
        prov.append(i+1)
    if visited == prov:
        return Ans
    else:
        return 'impossible'
def PSK(Tree):
    pass
Tree = MST()
print(MIN(Tree))