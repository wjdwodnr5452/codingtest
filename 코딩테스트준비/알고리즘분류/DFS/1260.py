import sys

n, m, v = map(int, sys.stdin.readline().split())

def dfs(graph, v, visited) :

    visited[v] = True
    print(v, end= ' ')

    for i in range(1, n+1) :
        if not visited[i] :
            dfs(graph, i, visited)


graph = [[]]
visited = [False] * (m+1)

for i in range(m) :
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)

dfs(graph, v, visited)