"""def read_graph_as_edges_w():
    n = int(input())
    graph = [[0,0] for i in range(n)]
    proverka = []
    a = 0
    for i in range(n):
        b = list(map(str, input().split()))
        shit = -1
        ut = -1
        v = '<'
        if v in b:
            b[0], b[2] = b[2], b[0]
        b.pop(1)
        for v in b:
            ut +=1
            if v not in proverka:
                graph[i][ut] = a
                proverka.append(v)
                proverka.append(a)
                a +=1
            else:
                graph[i][ut] = proverka[proverka.index(v)+1]

    return graph
def DFS(G, v, hasChycle, visited):
    visited[v] = 1
    for i in graph:
        if visited[i[-1]]==0:
            DFS(G, i[-1], hasChycle, visited)
    visited[v] = 2
    return visited
graph = read_graph_as_edges_w()
visited = DFS(graph, 0, False, [0 for i in range(len(graph))])
print(visited)
if 1 in visited:
    print('impossible')
else:
    print('possible')"""
'''
3
socrates > pluto
pluto > aristotles
socrates < aristotles
'''
"""
3
biber > dolik
oigen > biber
dolik < oigen
"""

"""def read_graph_as_edges_w():
    n = int(input())
    graph = [[0,0] for i in range(n)]
    proverka = []
    a = 0
    for i in range(n):
        b = list(map(str, input().split()))
        shit = -1
        ut = -1
        v = '<'
        if v in b:
            b[0], b[2] = b[2], b[0]
        b.pop(1)
        for v in b:
            ut +=1
            if v not in proverka:
                graph[i][ut] = a
                proverka.append(v)
                proverka.append(a)
                a +=1
            else:
                graph[i][ut] = proverka[proverka.index(v)+1]

    return graph
def DFS(graph, visited, v):
    visited[v] = 1
    has_Cycle = True
    for vertex in graph[v]:
        if visited[vertex] == 1:
            return False
        if visited[vertex] == 2:
            continue
        has_Cycle = DFS(graph, visited, vertex)
    visited[v] = 2
    return has_Cycle
graph = read_graph_as_edges_w()

if DFS(graph, [0 for i in range(len(graph))], 0):
    print("impossible")
else:
    print("possible")"""
n= int(input())
graph = {}
name_ids = {}
v = 0
def get_id(name,v):
    if name not in name_ids:
        name_ids[name] = v
    return name_ids[name]

while n!=0:
    request = input()
    if request.count('>'):
        source, target = request.split(" > ")
        source_id = get_id(source,v)
        v+=1
        target_id = get_id(target,v)

        if source_id in graph:
            graph[source_id].add(target_id)
        else:
            graph[source_id] = {target_id}
    else:
        target, source = request.split(" < ")
        source_id = get_id(source,v)
        v+=1
        target_id = get_id(target,v)

        if source_id in graph:
            graph[source_id].add(target_id)
        else:
            graph[source_id] = {target_id}
    n-=1
    v+=1
def DFS(graph, visited, v):
    visited[v] = 1
    has_Cycle = False
    for vertex in graph[v]:
        try:
            if visited[vertex] == 1:
                return True
            has_Cycle = DFS(graph, visited, vertex)
        except:
            return False
    visited[v] = 2
    return has_Cycle

if DFS(graph, dict.fromkeys(graph), 0):
    print("impossible")
else:
    print("possible")