import sys
sys.setrecursionlimit(10**8) 

n = int(input())

graph = []

graph_check = [[False for _ in range(n)] for _ in range(n)]

result = []

count = 0

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    global count

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[x][y] == 1 and not graph_check[x][y]:
        count += 1
        graph_check[x][y] = True

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx, ny)

for i in range(n) :
    graph.append(list(map(int, input())))

for i in range(n) :
    for j in range(n) :
        if not graph_check[i][j] and graph[i][j] == 1 : 
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()

print(len(result))

for i in result:
    print(i)

