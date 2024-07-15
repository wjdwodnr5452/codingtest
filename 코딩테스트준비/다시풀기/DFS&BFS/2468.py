import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

graph = []

max_hight = 0


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(h,x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if((0 <= nx < n) and (0 <= ny < n) and not graph_check[nx][ny] and graph[nx][ny] > h) :
            graph_check[nx][ny] = True
            dfs(h, nx, ny)
       
        
for i in range(n) :
    m = list(map(int, input().split()))
    graph.append(m)
    if(max(m) > max_hight) :
        max_hight = max(m)

result = 1

for i in range(max_hight) :
    graph_check = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for j in range(n) :
        for k in range(n) :
            if graph[j][k] > i and not graph_check[j][k] :
                count += 1
                graph_check[j][k] = True
                dfs(i,j,k)
                
    result = max(result, count)

print(result)


