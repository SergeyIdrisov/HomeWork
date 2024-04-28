"""
Надо немножко подумать
Самое тяжёлое ребро заменить спутником
Минимальное остовое дерево через Прим
Отсортировать по х слева направа и идти по точкам с меньшего к большему
и прибавлять к остову ближайшие точки
Берём n/2 последних рёбер и удаляем их.
Ответ: Самое тяжёлое оставшееся ребро.
"""
n = int(input())
v, u = map(int, input().split())
v /= 2
def MST():
    Edges = [[0,0]]
    for i in range(u):
        star = list(map(int, input().split()))
        weight = ((star[0]-Edges[i][-2])**2 + (star[1]-Edges[i][-1])**2)**0.5
        Edges.append([weight, star[0], star[1]])
    Edges.sort()

    return Edges
def MIN(Edges):
    for i in range(int(v)):
        Edges.pop(-1)
    print(f'{Edges[-1][0]:.{2}f}')
Tree = MST()
MIN(Tree)