import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []


def dfs(h, x, y) :
    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]
        if(0 <= nx < n) and (0 <= ny < n) and not check_graph[nx][ny] and graph[nx][ny] > h :
            check_graph[nx][ny] = True
            dfs(h, nx, ny)

for i in range(n) :
    m = list(map(int, sys.stdin.readline().split()))
    graph.append(m)

result = 1

for i in range(max(map(max, graph))) :
    check_graph = [[False for _ in range(n)] for _ in range(n)]
    count  =  0
    for j in range(n) :
        for k in range(n):
            if graph[j][k] > i and not check_graph[j][k] :
                count += 1
                check_graph[j][k] = True
                dfs(i, j, k)
    result = max(result, count)
       
print(result)