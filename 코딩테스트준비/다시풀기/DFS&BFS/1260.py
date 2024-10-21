import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
check_dfs = [False for _ in range(n+1)]
check_bfs = [False for _ in range(n+1)]

def dfs(start) :
    
    check_dfs[start] = True 
    print(start, end= ' ')

    graph[start].sort()

    for i in graph[start] :
        if not check_dfs[i] :
            dfs(i)


def bfs(start) :
    que = deque([start])
    check_bfs[start] = True

    while que :
        target = que.popleft()
        print(target, end= ' ')

        graph[target].sort()

        for i in graph[target] :
            if not check_bfs[i] :
                que.append(i)
                check_bfs[i] = True
    


for i in range(m) : 
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(v)
print()
bfs(v)
