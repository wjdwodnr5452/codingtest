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

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if((0 <= nx < n) and (0 <= ny < n)) and not graph_check[nx][ny] and graph[nx][ny] == 1:
            count += 1
            graph_check[nx][ny] = True
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

