def task_array_by_Dijkstra(graph):
    distances = {}
    visited = []
    end = []
    flag = True
    v = min(list(graph.keys()))
    for key in graph.keys():
        distances[key] = float('infinity')
    distances[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        current_node = visited.pop(0)
        end.append(current_node[1])
        for neighbor in graph[current_node[1]]:
            if neighbor[0] not in end:
                if (distances[current_node[1]] + neighbor[1]) < distances[neighbor[0]]:
                    distances[neighbor[0]] = (distances[current_node[1]] + neighbor[1])
                visited.append(neighbor[::-1])
            if distances[neighbor[0]] < 0:
                flag = False
                break

    return flag