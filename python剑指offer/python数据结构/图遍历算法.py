'''

度优先搜索(DFS)，该算法使用堆栈记住在任何迭代中发生死角时开始搜索的下一个顶点。

    B------D ------ F
  / |     /|
A   |   /  |
 \  |  /   |
  \ | /    |
   C-------E

使用stack实现DFS，使用Queue实现BFS.
'''

graph = {
    "A":["B", "C"],
    "B":["A", "C", "D"],
    "C":["A", "B", "D", "E"],
    "D":["B", "C", "E", "F"],
    "E":["C", "D"],
    "F":["D"]
}

# print(graph.keys())

def BFS(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    parent = {start: None}
    while (len(queue) > 0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w  not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


# def DFS(graph, start):
#     stack = []
#     stack.append(start)
#     seen = set()
#     seen.add(start)
#     while len(stack) > 0 :
#         vertex = stack.pop()
#         nodes = graph[vertex]
#         for w in nodes:
#             if w not in seen:
#                 stack.append(w)
#                 seen.add(w)
#         print(vertex)






print("广度优先搜索：")
parents = BFS(graph, "A")
print("打印所有节点的前一个节点：")
for key in parents:
    print(key, parents[key])
print("寻找最短路径：")
v = "F"
while v is not None:
    print(v)
    v = parents[v]

# print("\n")
# print("深度优先搜索：")
# DFS(graph, "A")