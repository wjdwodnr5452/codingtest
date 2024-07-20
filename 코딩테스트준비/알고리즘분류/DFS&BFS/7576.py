# 익은 토마토 1, 익지 않은 토마토 0, 토마토가 들어있지 않은 칸 -1
# 왼쪽, 오른쪽, 앞, 뒤 네 방향으로 토마토 영향

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
    # que 등록
    que = deque()

    for i in check_arr :
        que.append(i)

    while que :

        x, y = que.popleft()

        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            
            if((0<=nx < n) and ((0<=ny < m)) and graph[nx][ny] == 0) :
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                
                
graph = []

check_arr = []

for i in range(n) :
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(n) :
    for j in range(m) :
        if(graph[i][j] == 1) :
            check_arr.append([i,j])

# bfs 호출
bfs()

result = 0

for i in range(n) :
    for j in range(m) :
        if(graph[i][j] == 0) :
            result = -1
            print(result)
            exit()
        else :
            if(result < graph[i][j]) :
                result = graph[i][j] - 1
print(result)

