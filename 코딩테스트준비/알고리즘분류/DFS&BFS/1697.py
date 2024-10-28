import sys
from collections import deque


def bfs(v) :
    que = deque()
    que.append(v)

    while que :
        v = que.popleft()

        if v == k :
            print(graph[k])
            break

        for nx in (v-1, v+1, v*2) :
            if 0 <= nx <= max and not graph[nx] :
                graph[nx] = graph[v] + 1
                que.append(nx)
        


n, k = map(int, sys.stdin.readline().split())

max = 10 ** 5

graph = [0 for _ in range(max+1)]


bfs(n)





