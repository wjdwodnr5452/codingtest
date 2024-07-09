import sys
from collections import deque


def dfs(v) : 
    check_graph1[v] = True
    print(v, end= ' ')

    for i in range(1, n+1) :
        if not check_graph1[i] and graph[v][i] == 1:
            dfs(i)


def bfs(v) : 
    check_graph2[v] = True
    que = deque()
    que.append(v)

    while que :
        v = que.popleft()
        print(v, end= ' ')

        for i in range(1, n+1) :
            if not check_graph2[i] and graph[v][i] == 1:
                que.append(i)
                check_graph2[i] = True


    
n, m, v = map(int, sys.stdin.readline().split())


graph = [[0 for i in range(n+1)] for _ in range(n+1)]

check_graph1 = [False for _ in range(n+1)]
check_graph2 = [False for _ in range(n+1)]  

for i in range(m) : 
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs(v)
print()
bfs(v)

