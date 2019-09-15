graph = {
    "A":["B", "C"],
    "B":["A", "C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B", "C", "E", "F"],
    "E":["C", "D"],
    "F":["D"]
}


def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start: None}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent

parents = BFS(graph, "A")
print('-'*50)
target = "E"
while target != None:
    print(target)
    target = parents[target]
