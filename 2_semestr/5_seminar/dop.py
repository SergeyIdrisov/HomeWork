import sys
from collections import namedtuple
from functools import cmp_to_key

Edge = namedtuple('Edge', ['u', 'v', 'dist'])

mas = []
size = []


def Repr(n):
    while n != mas[n]:
        n = mas[n]
    return n


def Union(x, y):
    x = Repr(x)
    y = Repr(y)
    if x == y:
        return False
    mas[y] = x
    return True


class MyFun:
    def __call__(self, a, b):
        return a.dist - b.dist


if __name__ == "__main__":
    n, m, p = map(int, input().split())
    mas = [i for i in range(n + 1)]

    danger = [0] * (n + 1)
    u = list(map(int, input().split()))
    for _ in range(p):
        danger[u[_]] = float('inf')
    e = []
    dist = 0
    for _ in range(m):
        u, v, dist = map(int, input().split())
        if danger[u] > 0 and danger[v] == 0:
            danger[u] = min(danger[u], dist)
        if danger[v] > 0 and danger[u] == 0:
            danger[v] = min(danger[v], dist)
        if danger[u] == 0 and danger[v] == 0:
            e.append(Edge(u, v, dist))

    if m == 0:
        print("0")
        sys.exit(0)

    if m == 1:
        print(dist)
        sys.exit(0)

    e.sort(key=cmp_to_key(MyFun()))

    cnt = 0
    res = 0
    for edge in e:
        if Union(edge.u, edge.v):
            res += edge.dist
            cnt += 1

    for i in range(1, n + 1):
        if danger[i] > 0:
            res += danger[i]
            cnt += 1

    if cnt != n - 1 or res > sys.maxsize:
        print("impossible")
    else:
        print(res)
